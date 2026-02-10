from fastapi import APIRouter
from db import get_db
from sqlalchemy.orm import Session
import models
import schemas
from fastapi import Depends
from fastapi import HTTPException,status
from hashing import Hash
from repositry import user

router = APIRouter(
    prefix="/user",
    tags=["users"]
)




@router.post("/", response_model=schemas.ShowUser)
def creat_user(request:schemas.User,db:Session=Depends(get_db)):
    return user.create(request,db)



@router.get("/{id}",response_model=schemas.ShowUser)
def show_user_by_id(id:int,db:Session=Depends(get_db)):
    return user.show(id,db)