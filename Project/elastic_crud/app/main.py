import uvicorn
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from app.core.elastic import init_elasticsearch
from app.api.product_routes import router as product_router
from app.core.exceptions import NotFoundError, ElasticsearchError

app = FastAPI(
    title="FastAPI + Elasticsearch Demo",
    version="1.0.0"
)

@app.exception_handler(NotFoundError)
def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content={"error": exc.message}
    )


@app.exception_handler(ElasticsearchError)
def elastic_error_handler(request: Request, exc: ElasticsearchError):
    return JSONResponse(
        status_code=500,
        content={"error": exc.message}
    )

@app.on_event("startup")
def on_startup():
    """
    This runs once when the application starts.
    Similar to:
    - SQLAlchemy create_all()
    - MongoDB schema initialization
    """
    init_elasticsearch()

app.include_router(
    product_router,
    prefix="/products",
    tags=["Products"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the ElasticSearch CRUD API"}




# if __name__ == "__main__":
#     uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
# uv pip install "fastapi[standard]"
# uv run uvicorn app.main:app --reload
