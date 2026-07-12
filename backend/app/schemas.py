from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DocumentCreate(BaseModel):

    title : str
    content : str

class DocumentUpdate(BaseModel):

    title : Optional[str] = None
    content : Optional[str] = None

class DocumentResponse(BaseModel):

    id : int
    title : str

class DocumentChat(BaseModel):

    chat : str

class ChatResponse(BaseModel):

    content :str

class ChatMessage(BaseModel):

    id : int
    role : str
    content : str
    created_at : datetime

    model_config = {"from_attributes": True}