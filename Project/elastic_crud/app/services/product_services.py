# app/services/product_service.py

from uuid import uuid4
from datetime import datetime
from elasticsearch import Elasticsearch
from app.core.config import settings
from elasticsearch.exceptions import NotFoundError as ESNotFound
from app.core.exceptions import ElasticsearchError, NotFoundError

def create_product(data: dict,es_client: Elasticsearch):
    product_id = str(uuid4())

    document = {
        "id": product_id,
        **data,
        "created_at": datetime.utcnow()
    }

    try:
        es_client.index(
            index=settings.PRODUCT_INDEX,
            id=product_id,
            document=document,
            refresh="wait_for"
        )

        return document
    except ElasticsearchError:
        raise Exception("Some error occurred while creating product")
    

def get_product_by_id(product_id: str,es_client: Elasticsearch):
    try:
        result = es_client.get(
            index=settings.PRODUCT_INDEX,
            id=product_id
        )
        return result["_source"]
    except ESNotFound:
        raise NotFoundError(f"Product with id {product_id} not found")


def update_product(product_id: str, data: dict,es_client: Elasticsearch):
    try:
        es_client.update(
            index=settings.PRODUCT_INDEX,
            id=product_id,
            doc=data,
            refresh="wait_for"
        )

        return get_product_by_id(product_id,es_client)
    except ESNotFound:
        raise NotFoundError(f"Product with id {product_id} not found")


def delete_product(product_id: str,es_client: Elasticsearch):
    try:
        es_client.delete(
            index=settings.PRODUCT_INDEX,
            id=product_id,
            refresh="wait_for"
        )
    except ESNotFound:
        raise NotFoundError(f"Product with id {product_id} not found")


def list_products(
    es_client: Elasticsearch,
    page: int = 1,
    limit: int = 10,
    brand: str | None = None
):
    from_ = (page - 1) * limit

    filters = []
    if brand:
        filters.append({"term": {"brand": brand}})

    query = {
        "from": from_,
        "size": limit,
        "query": {
            "bool": {
                "filter": filters
            }
        }
    }

    try:
        result = es_client.search(
            index=settings.PRODUCT_INDEX,
            body=query
        )

        return [hit["_source"] for hit in result["hits"]["hits"]]
    except ElasticsearchError:
        raise Exception("Some error occurred while listing products")
