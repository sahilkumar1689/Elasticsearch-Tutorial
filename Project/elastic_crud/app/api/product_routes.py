# app/api/product_routes.py

from fastapi import APIRouter, Depends
from app.model.product_schema import ProductCreate, ProductUpdate
from app.services.product_services import (
    create_product,
    get_product_by_id,
    update_product,
    delete_product,
    list_products
)
from app.core.dependencies import get_es_client

router = APIRouter()

@router.post("/")
def create(data: ProductCreate,es_client=Depends(get_es_client)):
    return create_product(data.dict(),es_client=es_client)


@router.get("/{product_id}")
def get_by_id(product_id: str, es_client=Depends(get_es_client)):
    return get_product_by_id(product_id, es_client=es_client)


@router.put("/{product_id}")
def update(product_id: str, data: ProductUpdate, es_client=Depends(get_es_client)):
    return update_product(
        product_id,
        data.dict(exclude_unset=True),
        es_client=es_client 
    )


@router.delete("/{product_id}")
def delete(product_id: str, es_client=Depends(get_es_client)):
    delete_product(product_id, es_client=es_client)
    return {"message": "Product deleted"}


@router.get("/")
def list_all(
    page: int = 1,
    limit: int = 10,
    brand: str | None = None, es_client=Depends(get_es_client)
):
    return list_products(es_client,page, limit, brand)