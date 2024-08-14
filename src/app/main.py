from fastapi import FastAPI
from api.endpoints import view

app = FastAPI()


app.include_router(view.router)
