import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from db import test_db
from router.authenticate import auth_router
from router.msg import msg_router
from router.theme import theme_router

load_dotenv()
app = FastAPI()

origins = [
    os.getenv("FE_URL"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

test_db()

app.mount("/uploads/msg", StaticFiles(directory="uploads/msg"), name="msg_media")
app.mount("/uploads/bg", StaticFiles(directory="uploads/bg"), name="bg")
app.include_router(auth_router)
app.include_router(msg_router)
app.include_router(theme_router)
