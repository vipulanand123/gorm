from fastapi import FastAPI, status
from database import Base, engine, ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session
class ToDoRequest(BaseModel):
    task: str

Base.metadata.create_all(engine)

app = FastAPI()
@app.get('/')
def root():
    return {'message': 'Hello todo World'}

@app.post('/todo', status_code=status.HTTP_201_CREATED)
def create_todo(todo:ToDoRequest):
    session = Session(bind=engine, expire_on_commit = False)
    tododb = ToDo(task = todo.task)
    session.add(tododb)
    session.commit()

    id = tododb.id
    session.close()

    return f'create todo item with id {id}'
@app.get('/todo/{id}')
def read_todo(id:int):
    session = Session(bind=engine, expire_on_commit = False)
    todo = session.query(ToDo).get(id)
    session.close()
    return f'read todo item with id {id} and task {todo.task}'

@app.put('/todo/{id}')
def update_todo(id:int):
    return 'update todo item with id {}'.format(id)

@app.delete('/todo/{id}')
def delete_todo(id:int):
    return 'delete todo item with id {}'.format(id)

@app.get('/todo')
def read_todo_list():
    return 'read all todo items'
