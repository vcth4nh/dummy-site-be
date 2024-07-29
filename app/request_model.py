from typing import Annotated

from fastapi import Form, UploadFile
from pydantic import BaseModel


class Message(BaseModel):
    content: Annotated[str, Form()] = None
    img: UploadFile | None = None
