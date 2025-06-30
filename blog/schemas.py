from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(Blog):
    title: str
    body: str
    # pass
    class Config():
        orm_mode = True  # This allows Pydantic to read data from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # and convert it to a Pydantic model.

class User(BaseModel):
    name: str
    email:str
    passsword: str

class ShowUser(BaseModel):
    name: str
    email:str
    class Config():
        orm_mode = True