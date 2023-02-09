from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# # Series 1
#
# @app.get('/')
# async def hello_world():
#     return {"Hello": "World"}

# # Series 2

# @app.get("/component/{component_id}")  # path parameter
# async def get_component(component_id: int):
#     return {"component_id": component_id}
#
#
# @app.post("/component/")
# async def read_component(number: int, text: Optional[str] = None):  # query parameter
#     return {"number": number, "text": text}

# # Series 3

# class Package(BaseModel):
#     name: str
#     number: str
#     description: Optional[str] = None
#
#
# @app.get('/')
# async def hello_world():
#     return {'Hello' : 'World'}
#
# @app.post("/package/{priority}")
# async def make_package(priority: int, package: Package, value: bool):
#     return {"priority": priority, **package.dict(), "value": value}

# # Series 4
#
# class PackageIn(BaseModel):
#     secret_id: int
#     name: str
#     number: str
#     description: Optional[str] = None
#
#
# class Package(BaseModel):
#     name: str
#     number: str
#     description: Optional[str] = None
#
#
# @app.get('/')
# async def hello_world():
#     return {'Hello': 'World'}
#
#
# @app.post("/package/", response_model=Package,
#           response_model_include={"description"})  # response_model_exclude -> to exclude certain fields
# async def make_package(package: PackageIn):
#     return package

# # Series 5

class Todo(BaseModel):
    name: str
    due_date: str
    description: str


# app = FastAPI(title="Todo API")

# Create, Read, Update, Delete

store_todo = []


@app.get('/')
async def home():
    return {"Hello": "World"}


@app.post('/todo/')
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo


@app.get("/todo/", response_model=List[Todo])
async def get_all_todos():
    return store_todo


@app.get("/todo/{id}")
async def get_todo(id: int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.put("/todo/{id}")
async def update_todo(id: int, todo: Todo):
    try:
        store_todo[id] = todo
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.delete('/todo/{id}')
async def delete_todo(id: int):
    try:
        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")
