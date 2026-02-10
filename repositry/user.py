from fastapi import Depends
from db import get_db
from sqlalchemy.orm import Session
import models
import schemas
from hashing import Hash
from fastapi import HTTPException,status



def create(request:schemas.User,db:Session=Depends(get_db)):
    new_user = models.User(name = request.name,email=request.email,password=Hash.make(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id:int,db:Session=Depends(get_db)):
    getUser=db.query(models.User).filter(models.User.id == id ).first()
    if getUser is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not found")
    return getUser