from fastapi import FastAPI, HTTPException,status

UserAlreadyExistsException=HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Пользователь уже существует'
)
  
IncorrectEmailOrPasswordException=HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Неверная почта или пароль'
)


TokenExpiredException=HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Токен истек'
)

TokenAbsentException=HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Токен отсутсвует'
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED
)

UserIsNotPresentException=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)