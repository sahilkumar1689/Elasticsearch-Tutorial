# app/mappings/product_mapping.py

PRODUCT_MAPPING = {
    "mappings": {
        "properties": {
            "id": {
                "type": "keyword"
            },
            "name": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "brand": {
                "type": "keyword"
            },
            "price": {
                "type": "integer"
            },
            "in_stock": {
                "type": "boolean"
            },
            "created_at": {
                "type": "date"
            }
        }
    }
}
