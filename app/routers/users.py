

from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from .. import utils
from typing import List

router = APIRouter(
    tags=["Users"]
)

@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(usr: schemas.UserIn, db : Session= Depends(get_db)):
    print(usr.dict())
    hashed_password = utils.hash(usr.password)
    usr.password = hashed_password
    new_usr=models.Users(**usr.dict())
    db.add(new_usr)
    db.commit()
    db.refresh(new_usr)
    return new_usr

@router.get('/user/{id}', response_model=schemas.UserOut)
async def users(id: int, db : Session= Depends(get_db)):
    ret = db.query(models.Users).filter(models.Users.id == id).first()
    return ret

@router.get('/user', response_model=List[schemas.UserOut])
async def users(db : Session= Depends(get_db)):
    ret = db.query(models.Users).all()
    return ret