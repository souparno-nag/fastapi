from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session 
from .. import schemas, database, models

router = APIRouter()

@router.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title = request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} not found')
    blog.update(request)
    db.commit()
    return 'updated'


@router.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id: int, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # return {'error': 'Blog not found'}
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f'Blog with the id {id} not available'}
    return blog