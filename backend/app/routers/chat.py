from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.DAL import message as msg_dal
from app import schemas
from app.services.chat import chat_with_document

router = APIRouter(
    prefix="/document/{document_id}",
    tags=["chat"]
)

@router.get('/chat', response_model=list[schemas.ChatMessage])
async def get_chat_history(
    document_id: int,
    db: AsyncSession = Depends(get_db)
):
    messages = await msg_dal.get_all_messages(document_id, db)
    return messages

@router.post('/chat', response_model=schemas.ChatResponse)
async def chat_with_document_endpoint(
    document_id: int,
    body: schemas.DocumentChat,
    db: AsyncSession = Depends(get_db)
):
    result = await chat_with_document(body, document_id, db)
    if not result:
        raise HTTPException(status_code=404, detail="Document not found")
    return result
