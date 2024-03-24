from pydantic import BaseModel

class DataTable(BaseModel):
    columns: list
    rows: list

class Matrix(BaseModel):
    matrix: list
    
class LGBMData(BaseModel):
    columns: list
    rows: list
    product_id: str