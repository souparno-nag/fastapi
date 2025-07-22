from pydantic import BaseModel
from typing import List

# class Blog(BaseModel):
#     title: str
#     body: str
#     class Config():
#         orm_mode = True

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email:str
    password: str

class ShowUser(BaseModel):
    name: str
    email:str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser
    # pass
    class Config():
        orm_mode = True  # This allows Pydantic to read data from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # and convert it to a Pydantic model.

class Login(BaseModel):
    username: str
    password: str