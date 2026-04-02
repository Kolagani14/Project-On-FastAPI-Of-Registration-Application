from fastapi import APIRouter, Request,Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse
from sqlmodel import Session,select
from typing import Annotated
from pydantic import EmailStr
from app.database import get_session
from app.user_models import CreateUser
router = APIRouter()
session_depends=Annotated[Session,Depends(get_session)]
templates=Jinja2Templates(directory="app/templates")
@router.get("/",response_class=HTMLResponse)
def register_form(request:Request):
    return templates.TemplateResponse("register.html",{"request":request})
@router.post("/register")
def register_user(session:session_depends,name:str=Form(...),email:EmailStr=Form(...),phone:int=Form(...),):
    user=CreateUser(name=name,email=email,phone=phone)
    session.add(user)
    session.commit()
    return RedirectResponse(url="/user",status_code=303)
@router.get("/user",response_class=HTMLResponse)
def user_form(session:session_depends,request:Request):
    users=session.exec(select(CreateUser)).all()
    return templates.TemplateResponse("user.html",{"request":request,"users":users})