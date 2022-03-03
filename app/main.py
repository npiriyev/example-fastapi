
from typing import Optional, List
import fastapi
from fastapi import Body, Depends, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from app.routers.users import users
from .database import engine, Base, get_db
from . import models
from . import schemas
from . import utils
from sqlalchemy.orm import Session
from .routers import users, auth

app = FastAPI()

# while True:
#     try:
#         conn = psycopg2.connect(database="fastapi", user="postgres", password="postgres", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Successfully connected to Database!")
#         break
#     except Exception as error:
#         print("Error: ", error)
#         time.sleep(4)




Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)




class Posts(BaseModel):
    title : str
    owner: str
    privacy : Optional[bool] = None


    

@app.post('/posts/{id}')
async def smth(payload: Posts, id: int):
    # print(payload.title)
    # cursor.execute("""
    # update posts set title = %s, owner = %s where id = %s returning *
    # """, (payload.title, payload.owner, str(id)))
    # ret=cursor.fetchall()
    # conn.commit()
    # print(ret)
    # return {"message": ret}
    pass

@app.get('/orm')
async def ormm(db : Session= Depends(get_db)):
    ret = db.query(models.Posts).all()
    
    return {"message": ret}

@app.get('/')
async def root():
    return {"message": 'Success'}

@app.get('/posts')
async def get_posts():
    # cursor.execute("""
    # insert into posts(title,owner) values (%s,%s) returning *
    # """, ('smth1', 'nikk1'))
    # ret=cursor.fetchall()
    # conn.commit()
    # print(ret)
    # return {"message": ret}
    pass

@app.get('/all_posts')
async def get_posts():
    # cursor.execute("""
    # select * from posts
    # """)
    # ret=cursor.fetchall()
    # print(ret)
    # return {"message": ret}
    pass

@app.post('/')
async def index(payload : Posts):
    
    print(payload.dict())
    return {"message": payload.dict()}

@app.get('/{id}', status_code=status.HTTP_201_CREATED)
async def root(id:int):
    if type(id) != int:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id is not an integer")
    return {"message":"smth"}
    # Response(status_code=status.HTTP_202_ACCEPTED)

