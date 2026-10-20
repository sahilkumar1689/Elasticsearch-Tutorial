# app/core/elastic.py

from elasticsearch import Elasticsearch
from app.core.config import settings
from app.mapping.product_mapping import PRODUCT_MAPPING

es_client = Elasticsearch(
    settings.ELASTIC_URL,
    api_key=settings.ELASTIC_API_KEY
)

def init_elasticsearch():
    """
    Create index if it does not exist.
    Equivalent to DB schema creation.
    """
    if not es_client.indices.exists(index=settings.PRODUCT_INDEX):
        es_client.indices.create(
            index=settings.PRODUCT_INDEX,
            body=PRODUCT_MAPPING
        )
