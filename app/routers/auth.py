from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from .. import utils
from typing import List

router = APIRouter(
    tags=["Auth"]
)

@router.post('/login')
async def login(usr : schemas.UserIn, db: Session=Depends(get_db)):
    # return {"success"}
    ret = db.query(models.Users).filter(models.Users.email == usr.email).first()
    if not ret:
        return {"Invalid credentials!"}
    ret=utils.check_hash(usr.password, ret.password)
    print(ret)
    if not ret:
        return {"Invalid credentials!"}
    return {"success"}
