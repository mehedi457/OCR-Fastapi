from fastapi import FastAPI
from router import ocr

app = FastAPI()

app.include_router(ocr.router)




