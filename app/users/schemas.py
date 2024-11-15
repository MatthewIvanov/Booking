from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    passsword: str

    class Config:
        #orm_mode = True
        from_attributes = True
