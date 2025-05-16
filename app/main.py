from fastapi import FastAPI
from app.apis.routes import router

app = FastAPI(title="Auth Service")
app.include_router(router)