from pydantic import BaseModel
from typing import List




# ---------- BLOG ----------
class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        from_attributes = True


# ---------- USER ----------
class User(BaseModel):
    name: str
    email: str
    password: str   


class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True


class ShowUser(UserBase):
    blogs: List[Blog]


# ---------- SHOW BLOG ----------
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: UserBase

    class Config:
        from_attributes = True

# ---------- LOGIN ----------
class Login(BaseModel):
    username: str
    password: str


# ---------- TOKEN ----------
class Token(BaseModel):
    access_token: str
    token_type: str


# ---------- TOKEN DATA ----------
class TokenData(BaseModel):
    email: str | None = None