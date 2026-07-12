from fastapi import FastAPI
from app.routers import document, chat

app = FastAPI(title="INBOX")


@app.get('/')
async def home():
    return {'Status':1}

app.include_router(document.router)
app.include_router(chat.router)