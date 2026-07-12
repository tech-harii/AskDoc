from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app import models


async def get_all_messages(document_id: int, db: AsyncSession) -> list[models.Message]:
    result = await db.execute(
        select(models.Message)
        .where(models.Message.document_id == document_id)
        .order_by(models.Message.created_at)
    )
    return list(result.scalars().all())


async def get_message_history(document_id: int, db: AsyncSession) -> list[dict]:
    result = await db.execute(
        select(models.Message)
        .where(models.Message.document_id == document_id)
        .order_by(models.Message.created_at)
    )
    rows = result.scalars().all()
    return [{"role": msg.role, "content": msg.content} for msg in rows]


async def save_messages(document_id: int, user_message: str, assistant_reply: str, db: AsyncSession) -> None:
    user_msg = models.Message(document_id=document_id, role="user", content=user_message)
    assistant_msg = models.Message(document_id=document_id, role="assistant", content=assistant_reply)
    db.add_all([user_msg, assistant_msg])
    await db.commit()
