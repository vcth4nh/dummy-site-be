import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from router.authenticate import auth_router
from router.msg import msg_router

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

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(auth_router)
app.include_router(msg_router)
