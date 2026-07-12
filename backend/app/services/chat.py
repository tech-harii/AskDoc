from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas
from app.DAL import document as doc_dal
from app.DAL import message as msg_dal
from app.services.ai import get_ai_reply


async def chat_with_document(data: schemas.DocumentChat, document_id: int, db: AsyncSession) -> schemas.ChatResponse | None:
    document = await doc_dal.get_document_by_id(document_id, db)

    if not document:
        return None

    history = await msg_dal.get_message_history(document_id, db)

    reply = await get_ai_reply(document.content, history, data.chat)

    await msg_dal.save_messages(document_id, data.chat, reply, db)

    return schemas.ChatResponse(content=reply)
