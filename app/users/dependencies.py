from datetime import datetime
from fastapi import Depends, HTTPException,Request,status
from jose import jwt,JWTError
from app.config import settings
from app.users.dao import UsersDAO


def get_token(request:Request):
    token=request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token


async def get_current_user(token:str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token,settings.SECRET_KEY,settings.ALGORITHM
        )
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='jwt error')
    expire :str = payload.get('exp')
    if (not expire) or (int(expire)<datetime.now().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='datetime expire')
    user_id:str = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='not user_id')
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='find_by_id error')

    return user