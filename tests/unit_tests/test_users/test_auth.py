import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient
from pydantic import EmailStr

from app.config import settings
from app.main import app as fastapi_app


@pytest.mark.parametrize("email,password,status_code",[
    ("test@test.com","string",200),
    ("kot@pes.com","kot0pes",200),
    ("pes@kot.com","pesokot",200),
    ("abcde","pesokot",422),
])


async def test_register_user(email,password,status_code, ac:AsyncClient):
    response = await ac.post("/auth/register",json={
        "email": email,
        "password": password,
    })
    assert response.status_code==status_code


@pytest.mark.parametrize("email,password,status_code",[
    ("test@test.com","string",200),
    ("pes@kot.com","pesokot",200),
    ("abcde","pesokot",422),
])

async def test_login_user(email,password,status_code,ac:AsyncClient):
    response= await ac.post("/auth/login",json={
        "email":email,
        "password":password,
    })
    assert response.status_code==status_code
