from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app import models
from app.schemas import DocumentCreate, DocumentResponse, DocumentUpdate


async def create_document(data: DocumentCreate, db: AsyncSession) -> DocumentResponse:
    new_docu = models.Document(**data.model_dump())
    db.add(new_docu)
    await db.commit()
    await db.refresh(new_docu)

    return DocumentResponse(
        id=new_docu.id,
        title=new_docu.title
    )


async def get_document_by_id(document_id: int, db: AsyncSession) -> models.Document | None:
    result = await db.execute(
        select(models.Document).where(models.Document.id == document_id)
    )
    return result.scalar_one_or_none()


async def get_all_documents(db: AsyncSession) -> list[models.Document]:
    result = await db.execute(select(models.Document).order_by(models.Document.created_at.desc()))
    return list(result.scalars().all())


async def update_document(document_id: int, data: DocumentUpdate, db: AsyncSession) -> models.Document | None:
    document = await get_document_by_id(document_id, db)
    if not document:
        return None

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(document, field, value)

    await db.commit()
    await db.refresh(document)
    return document


async def delete_document(document_id: int, db: AsyncSession) -> bool:
    document = await get_document_by_id(document_id, db)
    if not document:
        return False

    await db.execute(
        delete(models.Message).where(models.Message.document_id == document_id)
    )
    await db.delete(document)
    await db.commit()
    return True
