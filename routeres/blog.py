from fastapi import APIRouter, Depends, status
from typing import List
from db import get_db
from sqlalchemy.orm import Session
import schemas
from repositry import blog
import aouth2


router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.post("/")
def create(request: schemas.Blog,db : Session=Depends(get_db),current_user: schemas.TokenData=Depends(aouth2.get_current_user)):
    return blog.create(request,db,current_user)


@router.get("/",response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user: schemas.TokenData=Depends(aouth2.get_current_user)):
   return blog.get_all_blogs(db)


@router.get("/{id}",status_code=200,response_model=schemas.ShowBlog)
def show(id:int,db:Session=Depends(get_db),current_user: schemas.TokenData=Depends(aouth2.get_current_user)):
   return blog.show(id,db)


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db),current_user: schemas.TokenData=Depends(aouth2.get_current_user)):
    return blog.destroy(id,db,current_user)
   

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.Blog,db:Session=Depends(get_db),current_user: schemas.TokenData=Depends(aouth2.get_current_user)):
    return blog.update(id,request,db,current_user)
   