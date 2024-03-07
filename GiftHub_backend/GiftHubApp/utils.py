from django.db import connections
from django.db.utils import OperationalError
import pandas as pd
import json

def db_get_seq(db, table) -> int:
    try:
        with connections[db].cursor() as cursor:
            cursor.execute(f"SELECT nextval({table}_seq) FROM dual")
            seq = cursor.fetchall()[0][0]
    except OperationalError as e:
        raise(f"db error: {e}")
    except Exception as e:
        raise(f"error: {e}")
        
    return seq

def db_get_matched_items(db, category_1, price_type) -> json:
    try:
        with connections[db].cursor() as cursor:
            cursor.execute(f"""
                            select a.product_id, a.product_url
                              from product a join (
                              select product_id, category_1
                                  from product_category
                              where category_1 = '개업선물'
                              group by product_id, category_1
                              ) b
                                  on a.product_id = b.product_id
                                  and a.price >= f_price_max('price_type', '1')
                                  and a.price <= f_price_max('price_type', '1')
                            """)
            columns = [col[0] for col in cursor.description]
            df = pd.DataFrame(cursor.fetchall(), columns=columns)
            df = df.sample(27)
            str_js = df.to_json(force_ascii=False, orient="records", indent=4)
            js = json.loads(str_js)
            
    except OperationalError as e:
        raise(f"db error: {e}")
    except Exception as e:
        raise(f"error: {e}")
        
    return js