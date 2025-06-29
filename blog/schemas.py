from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(Blog):
    # pass
    class Config:
        orm_mode = True  # This allows Pydantic to read data from ORM models
        # It tells Pydantic to treat the SQLAlchemy model as a dictionary
        # and convert it to a Pydantic model.