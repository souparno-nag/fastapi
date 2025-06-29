from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/blog")
def index(limit=10, published: bool=True, sort: Optional[str] = None):
    if published:
        return {"data": f'{limit} published blogs from the db'}
    else:
        return {"data": f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get("/blog/{id}")
def display(id: int):
    return {"data": id}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data' : {'1', '2'}}

@app.get("/about")
def about():
    return {"data": "about page"}

# @app.post('/blog')
# def create_blog():
#     return {'data': 'Blog is created'}

class Blog(BaseModel):
    # pass
    title: str
    body: str
    published_at: Optional[bool] = None

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': 'Blog is created with title as {request.title}'}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)