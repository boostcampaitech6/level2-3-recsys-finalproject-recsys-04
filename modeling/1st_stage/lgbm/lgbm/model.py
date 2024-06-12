from lightgbm import LGBMClassifier
import numpy as np

class lgbm():
    def __init__(self, argument, all_data):
        self.argument = argument
        self.model = LGBMClassifier(
                                    objective='multiclass',
                                    learning_rate=argument.learning_rate,
                                    num_leaves=argument.num_leaves,
                                    n_estimators=argument.n_estimators,
                                    max_depth=argument.max_depth,
                                    verbose=-1,
                                )
    
    def fit(self, all_data):
        return self.model.fit(all_data[self.argument.features_col].values, all_data[self.argument.targets_col].values.ravel())
    


    
        