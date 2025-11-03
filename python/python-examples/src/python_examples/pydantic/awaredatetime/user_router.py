import logging as log
from fastapi import FastAPI

from .user import User

app = FastAPI()

@app.post("/")
def update_user(user: User) -> User:
    log.info(f"Received data {user}")
    return user