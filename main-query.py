from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# @app.get("/blog?limit=10&published=true")
# def index():
#     # only get 10 published blogs
#     return {"data": "blog list"}

# @app.get("/blog")
# def index(limit):
#     return {"data": f'{limit} blogs from the db'}

# @app.get("/blog")
# def index(limit, published):
#     # return published - published is a string
#     if published:
#         return {"data": f'{limit} published blogs from the db'}
#     else:
#         return {"data": f'{limit} blogs from the db'}

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

# @app.get('/blog/{id}/comments')
# def comments(id):
#     return {'data' : {'1', '2'}}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data' : {'1', '2'}}

@app.get("/about")
def about():
    return {"data": "about page"}
