# app/models/product_schema.py

from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    brand: str
    price: int
    in_stock: bool = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[int] = None
    in_stock: Optional[bool] = None

class ProductResponse(BaseModel):
    id: str
    name: str
    brand: str
    price: int
    in_stock: bool
