from fastapi import FastAPI, Depends, status, Response, HTTPException
# from pydantic import BaseModel
from . import schemas, models, hashing
from .database import engine, SessionLocal
from sqlalchemy.orm import Session 
from typing import List
from passlib.context import CryptContext
from blog.router import blog, user, authentication

app = FastAPI()

# @app.post('/blog')
# def create():
#     return 'creating'

# @app.post('/blog')
# def create(title, body):
#     return {'title': title, 'body': body}

# class Blog(BaseModel):
#     title: str
#     body: str

# @app.post('/blog')
# def create(request: Blog):
#     return {request}

models.Base.metadata.create_all(bind=engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# @app.post('/blog')
# def create(request: schemas.Blog):
#     return {request}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.post('/blog', status_code=201)

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
#     # return db
#     new_blog = models.Blog(title = request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# def destroy(id: int, db: Session = Depends(get_db)):
#     # blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} not found')
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
#     # pass
#     # db.query(models.Blog).filter(models.Blog.id == id).update({'title':'Updated title'})
#     # db.query(models.Blog).filter(models.Blog.id == id).update(request)
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} not found')
#     blog.update(request)
#     db.commit()
#     return 'updated'

# @app.get('/blog', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog], tags=['blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
# def show(id: int, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # return {'error': 'Blog not found'}
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {'detail': f'Blog with the id {id} not available'}
#     return blog

# pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @app.post('/user', response_model=schemas.ShowUser, tags=['users'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     # return request
    
#     # new_user = models.User(name = request.name, email=request.email, password=request.password)

#     # hashedPassword = pwd_cxt.hash(request.password)
#     # new_user = models.User(name = request.name, email=request.email, password=hashedPassword)
#     new_user = models.User(name = request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} not found')
#     return user