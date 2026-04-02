from sqlmodel import SQLModel,Field
from typing import Optional
from pydantic import EmailStr
class CreateUser(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
    email:EmailStr
    phone:int