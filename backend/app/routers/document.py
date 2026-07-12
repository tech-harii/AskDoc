from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import schemas
from app.DAL import document as doc_dal

router = APIRouter(
    prefix="/document",
    tags=["document"]
)


@router.get('/', response_model=list[schemas.DocumentResponse])
async def get_all_documents(db: AsyncSession = Depends(get_db)):
    return await doc_dal.get_all_documents(db)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.DocumentResponse)
async def create_docu(
    body: schemas.DocumentCreate, db: AsyncSession = Depends(get_db)
):
    return await doc_dal.create_document(body, db)

@router.get('/{document_id}', response_model=schemas.DocumentResponse)
async def get_document(document_id: int, db: AsyncSession = Depends(get_db)):
    document = await doc_dal.get_document_by_id(document_id, db)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.put('/{document_id}', response_model=schemas.DocumentResponse)
async def update_document(
    document_id: int,
    body: schemas.DocumentUpdate,
    db: AsyncSession = Depends(get_db)
):
    document = await doc_dal.update_document(document_id, body, db)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@router.delete('/{document_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(document_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await doc_dal.delete_document(document_id, db)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)