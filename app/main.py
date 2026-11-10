from fastapi import FastAPI
from app.config import settings

app = FastAPI(title="URL Shortner")

@app.get("/health")
async def health():
    return {"ok" : True ,
            "env" : settings.env}