from fastapi import FastAPI

app = FastAPI()

@app.get("/") # path operation decorator
def index(): # path operation function
    # return "Hey"
    # return {"data":{ "name": "Souparno"}}
    return {"data": "blog list"}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get("/blog/{id}")
def display(id: int):
    return {"data": id}

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments for a blog post where id = id
    return {'data' : {'1', '2'}}

# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data': 'all unpublished blogs'}

@app.get("/about")
def about(): # name of function does not matter
    return {"data": "about page"}