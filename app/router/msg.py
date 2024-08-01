from fastapi import APIRouter, status, Form, UploadFile, Depends
from typing import Annotated, Union
from router.authenticate import is_logged_in
from uuid import uuid4
import db

msg_router = APIRouter(
    prefix="/msg",
    tags=["msg"],
)


@msg_router.get("", status_code=status.HTTP_200_OK)
async def get_msg(offset: int = 0, length: int = 15, logged_in: bool = Depends(is_logged_in)):
    if offset < 0:
        offset = 0
    msg = db.get_msg(offset, length)
    msg.reverse()
    total = db.get_total_msg()
    return {
        "msg": msg,
        "total": total
    }


@msg_router.get("/{msgid}", status_code=status.HTTP_200_OK)
async def get_msgid(msgid: int, logged_in: bool = Depends(is_logged_in)):
    return db.get_msgid(msgid)


@msg_router.post("", status_code=status.HTTP_201_CREATED)
async def add_msg(msg: Annotated[str, Form()] = None,
                  file: Union[UploadFile, None] = None,
                  logged_in: bool = Depends(is_logged_in)):
    if msg is None and file is None:
        return {
            'debug': "Empty msg and file"
        }
    img_name = None
    if file:
        if file.size > 50 * 1024 * 1024:
            return {
                'debug': "File must <= 50MiB"
            }
        ext = file.filename.split(".")[-1]
        img_name = f"{uuid4().hex + ext}.{ext}"
        with open(f"uploads/{img_name}", "wb") as f:
            f.write(file.file.read())
    db.create_msg(msg, img_name)


@msg_router.delete("/{msgid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_msg(msgid: int, logged_in: bool = Depends(is_logged_in)):
    if msgid is None:
        return {
            'debug': "Empty msgid"
        }
    db.delete_msg(msgid)
