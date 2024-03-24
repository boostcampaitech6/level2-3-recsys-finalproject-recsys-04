import sys
import logging

import torch
import pandas as pd


class TorchEASE:
    def __init__(
        self, train, user_col="user_id", item_col="item_id", score_col=None, reg=250
    ):
        """

        :param train: Training DataFrame of user, item, score(optional) values
        :param user_col: Column name for users
        :param item_col: Column name for items
        :param score_col: Column name for scores. Implicit feedback otherwise
        :param reg: Regularization parameter
        """
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
            stream=sys.stdout,
        )

        self.logger = logging.getLogger("notebook")
        self.logger.info("Building user + item lookup")
        # How much regularization do you need?
        self.reg = reg

        self.user_col = user_col
        self.item_col = item_col

        self.user_id_col = user_col + "_id"
        self.item_id_col = item_col + "_id"

        self.user_lookup = self.generate_labels(train, self.user_col)
        self.item_lookup = self.generate_labels(train, self.item_col)

        self.item_map = {}
        self.logger.info("Building item hashmap")
        for _item, _item_id in self.item_lookup.values:
            self.item_map[_item_id] = _item

        train = pd.merge(train, self.user_lookup, on=[self.user_col])
        train = pd.merge(train, self.item_lookup, on=[self.item_col])
        self.logger.info("User + item lookup complete")
        self.indices = torch.LongTensor(
            train[[self.user_id_col, self.item_id_col]].values
        )

        if not score_col:
            # Implicit values only
            self.values = torch.ones(self.indices.shape[0])
        else:
            self.values = torch.FloatTensor(train[score_col])
        # TODO: Is Sparse the best implementation?

        self.sparse = torch.sparse.FloatTensor(self.indices.t(), self.values)

        self.logger.info("Sparse data built")

    def generate_labels(self, df, col):
        dist_labels = df[[col]].drop_duplicates()
        dist_labels[col + "_id"] = dist_labels[col].astype("category").cat.codes

        return dist_labels

    def fit(self):
        self.logger.info("Building G Matrix")
        self.G = self.sparse.to_dense().t() @ self.sparse.to_dense()
        self.G += torch.eye(self.G.shape[0]) * self.reg

        self.P = self.G.inverse()

        self.logger.info("Building B matrix")
        B = self.P / (-1 * self.P.diag())
        # Set diagonals to 0. TODO: Use .fill_diag_
        B = B + torch.eye(B.shape[0])

        # Predictions for user `_u` will be self.sparse.to_dense()[_u]@self.B
        self.B = B

        return

    def fine_tune(self, new_data):
        """
        Fine-tune the model with new data.

        :param new_data: New training DataFrame of user, item, score(optional) values
        """
        self.logger.info("Fine-tuning model with new data")

        # Update indices and values with new data
        new_user_ids = self.generate_labels(new_data, self.user_col)
        new_item_ids = self.generate_labels(new_data, self.item_col)

        new_data = pd.merge(new_data, new_user_ids, on=[self.user_col])
        new_data = pd.merge(new_data, new_item_ids, on=[self.item_col])

        new_indices = torch.LongTensor(new_data[[self.user_id_col, self.item_id_col]].values)

        
        new_values = torch.ones(new_indices.shape[0])
      

        # Update sparse matrix
        self.indices = torch.cat((self.indices, new_indices), dim=0)
        self.values = torch.cat((self.values, new_values), dim=0)
        self.sparse = torch.sparse.FloatTensor(self.indices.t(), self.values)

        # Update user lookup
        new_user_lookup = self.generate_labels(new_data, self.user_col)
        self.user_lookup = pd.concat([self.user_lookup, new_user_lookup]).drop_duplicates()

        # Re-calculate G matrix
        self.logger.info("Updating G Matrix")
        new_data_tensor = torch.sparse.FloatTensor(self.indices.t(), self.values)
        G_update = torch.matmul(new_data_tensor.to_dense().t(), new_data_tensor.to_dense())
        G_update += torch.eye(G_update.shape[0]) * self.reg
        
        # Ensure G_update has the same size as self.G
        if G_update.shape != self.G.shape:
            self.logger.error("Shape mismatch between G_update and self.G")
            print("G_update.shape", G_update.shape)
            print("self.G.shape", self.G.shape)
            return

        self.G = G_update

        # Re-calculate B matrix
        self.logger.info("Updating B Matrix")
        P = self.G.inverse()
        B = P / (-1 * P.diag())
        B += torch.eye(B.shape[0])
        self.B = B

        self.logger.info("Fine-tuning complete.")

        return

    def predict_all(self, pred_df, k=5, remove_owned=True):
        """
        :param pred_df: DataFrame of users that need predictions
        :param k: Number of items to recommend to each user
        :param remove_owned: Do you want previously interacted items included?
        :return: DataFrame of users + their predictions in sorted order
        """
        pred_df = pred_df[[self.user_col]].drop_duplicates()
        n_orig = pred_df.shape[0]

        # Alert to number of dropped users in prediction set
        pred_df = pd.merge(pred_df, self.user_lookup, on=[self.user_col])
        n_curr = pred_df.shape[0]
        if n_orig - n_curr:
            self.logger.info(
                "Number of unknown users from prediction data = %i" % (n_orig - n_curr)
            )

        _output_preds = []
        # Select only user_ids in our user data
        _user_tensor = self.sparse.to_dense().index_select(
            dim=0, index=torch.LongTensor(pred_df[self.user_id_col])
        )

        # Make our (raw) predictions
        _preds_tensor = _user_tensor @ self.B
        self.logger.info("Predictions are made")
        if remove_owned:
            # Discount these items by a large factor (much faster than list comp.)
            self.logger.info("Removing owned items")
            _preds_tensor += -1.0 * _user_tensor

        self.logger.info("TopK selected per user")
        for _preds in _preds_tensor:
            # Very quick to use .topk() vs. argmax()
            _output_preds.append(
                [self.item_map[_id] for _id in _preds.topk(k).indices.tolist()]
            )
            
        pred_df["predicted_items"] = _output_preds
        self.logger.info("Predictions are returned to user")
        return pred_df