from django.db import connections
from django.db.utils import OperationalError
import pandas as pd
import json

class SqlExecutor:
    def __init__(self, db):
        self.db = db
            
    def get_sql_to_json(self, sql) -> json:
        try:
            with connections[self.db].cursor() as cursor:
                cursor.execute(sql)
                columns = [col[0] for col in cursor.description]
                df = pd.DataFrame(cursor.fetchall(), columns=columns)
                str_js = df.to_json(force_ascii=False, orient="records", indent=4)
                js = json.loads(str_js)
        except OperationalError as e:
            raise(f"db error: {e}")
        except Exception as e:
            raise(f"error: {e}")
            
        return js

    def get_sql_to_df(self, sql) -> pd.DataFrame:
        try:
            with connections[self.db].cursor() as cursor:
                cursor.execute(sql)
                columns = [col[0] for col in cursor.description]
                df = pd.DataFrame(cursor.fetchall(), columns=columns)
        except OperationalError as e:
            raise(f"db error: {e}")
        except Exception as e:
            raise(f"error: {e}")
            
        return df
    
    def df_to_json(self, df: pd.DataFrame) -> json:
        str_js = df.to_json(force_ascii=False, orient="records", indent=4)
        js = json.loads(str_js)
        
        return js

def params_to_data(params) -> list:
    if len(params) == 0:
        return None
    list_data = []
    for k, v in params.items():
        if k.startswith("data_"):
            list_data.append(v)
    return list_data

def sql_get_user_id() -> str:
    sql = f"""
    SELECT nextval(user_seq) as user_id FROM dual
    """
    return sql

def sql_get_matched_items(**params: dict) -> str:
    data = params_to_data(params)
    sql = f"""
    select a.product_id, c.data_1 as image_url
    from product a join (
                        select product_id, category_1, category_2, category_3
                        from product_category
                        where category_1 = '{data[0]}'
                        ) b
    on a.product_id = b.product_id join commoninfo c
    on b.category_1 = c.key_1
    and b.category_2 = c.key_2
    and b.category_3 = c.key_3
    where a.price >= f_price_min('price_type', '{data[1]}')
    and a.price <= f_price_max('price_type', '{data[1]}')
    order by RAND() LIMIT 27
    """
    return sql

def sql_get_matched_items_back(**params: dict) -> str:
    data = params_to_data(params)
    sql = f"""
    select a.product_id, a.product_name, a.price, a.image_url
      from product a join (
                              select product_id, category_1
                                  from product_category
                              where category_1 = '{data[0]}'
                              group by product_id, category_1
                             ) b
        on a.product_id = b.product_id
     where a.price >= f_price_min('price_type', '{data[1]}')
       and a.price <= f_price_max('price_type', '{data[1]}')
     order by RAND() LIMIT 27
    """
    return sql

def sql_get_popular_items_top10(**params: dict) -> str:
    data = params_to_data(params)
    sql = f"""
    select product_id, product_name, price, image_url
    from (
            select ROW_NUMBER() OVER(PARTITION BY b.category_1, b.category_2, b.category_3 ORDER BY a.rating desc, a.num_review desc) as rank,
                a.product_id, a.product_name, a.brand, b.category_1, b.category_2, b.category_3, a.rating, a.num_review, a.price, a.image_url, a.product_url
            from product a join product_category b
                on a.product_id = b.product_id
            where (b.category_1, b.category_2, IFNULL(b.category_3, '')) in (
                                                                            select b.category_1, b.category_2, IFNULL(b.category_3, '')
                                                                            from product a join product_category b
                                                                                on a.product_id = b.product_id
                                                                            where a.product_id in (
                                                                                                    select b.product_id
                                                                                                    from user a join user_product_interaction b
                                                                                                        on a.user_id = b.user_id
                                                                                                    where a.user_id = '87'
                                                                                                    )
                                                                            group by b.category_1, b.category_2, b.category_3
                                                                            )
            and a.price >= f_price_min('price_type', '{data[1]}')
            and a.price <= f_price_max('price_type', '{data[1]}')
        ) A
    where rank <= 10
    order by rand() LIMIT 10
    """
    return sql

def sql_get_popular_items(**params: dict) -> str:
    data = params_to_data(params)
    sql = f"""
    select a.product_id, a.image_url
      from product a join (
                              select product_id, category_1
                                  from product_category
                              where category_1 = '{data[0]}'
                              group by product_id, category_1
                             ) b
        on a.product_id = b.product_id
     where a.price >= f_price_min('price_type', '{data[1]}')
       and a.price <= f_price_max('price_type', '{data[1]}')
     order by RAND() LIMIT 27
    """
    return sql

def sql_get_filtered_item(**params: dict) -> str:
    data = params_to_data(params)
    sql = f"""
    select product_id
      from filtered_rawdata
      where category_1 = '{data[0]}'
      and price >= f_price_min('price_type', '{data[1]}')
      and price <= f_price_max('price_type', '{data[1]}')
      order by rand() LIMIT 1
    """
    return sql