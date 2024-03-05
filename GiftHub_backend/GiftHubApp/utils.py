from django.db import connections
from django.db.utils import OperationalError

def db_get_seq(db, table) -> int:
    try:
        with connections[db].cursor() as cursor:
            cursor.execute(f"SELECT nextval({table}_seq) FROM dual")
            seq = cursor.fetchall()[0][0]
    except OperationalError as e:
        print(f"db error: {e}")
    except Exception as e:
        print(f"error: {e}")
        
    return seq