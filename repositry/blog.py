from fastapi import Depends
from db import get_db
from sqlalchemy.orm import Session
import models
import schemas
from fastapi import HTTPException,status


def create(request:schemas.Blog,db:Session,current_user:schemas.TokenData):
    user = db.query(models.User).filter(models.User.email == current_user.email).first()
    new_blog = models.Blog(title=request.title, body=request.body, user_id=user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def show(id:int,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not available")
    return blog



def destroy(id:int,db:Session,current_user:schemas.TokenData):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not found")
    
    # Authorization check
    user = db.query(models.User).filter(models.User.email == current_user.email).first()
    if blog.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to delete this blog")

    db.delete(blog)
    db.commit()
    return {"done"}


def update(id:int,request:schemas.Blog,db:Session,current_user:schemas.TokenData):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not found")
    
    # Authorization check
    user = db.query(models.User).filter(models.User.email == current_user.email).first()
    if blog.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to update this blog")

    blog.title = request.title
    blog.body = request.body
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return {"updated":blog}

