from typing import Annotated

from fastapi import Form, UploadFile
from pydantic import BaseModel


class Message(BaseModel):
    content: Annotated[str, Form()] = None
    img: UploadFile | None = None


class Theme(BaseModel):
    msg_color: Annotated[str, Form()] = None
    bg_color: Annotated[str, Form()] = None
    bg_img: UploadFile | None = None
