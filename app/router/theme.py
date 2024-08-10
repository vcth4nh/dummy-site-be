from typing import Annotated

from fastapi import APIRouter, status, Form, UploadFile, Depends

import db
from helper import upload_file
from router.authenticate import is_logged_in

theme_router = APIRouter(
    prefix="/theme",
    tags=["theme"],
)


@theme_router.get("", status_code=status.HTTP_200_OK)
async def get_theme(
        # logged_in: bool = Depends(is_logged_in)
):
    return db.get_theme()


@theme_router.put("", status_code=status.HTTP_201_CREATED)
async def set_dummy_theme(msg_color: Annotated[str, Form()] = None,
                          bg_color: Annotated[str, Form()] = None,
                          bg_img: UploadFile | None = None,
                          # logged_in: bool = Depends(is_logged_in)
                          ):
    print(msg_color, bg_color, bg_img)
    bg_img_path = upload_file(bg_img, 'bg')
    db.set_theme(msg_color, bg_color, bg_img_path)

# @theme_router.put("reset", status_code=status.HTTP_201_CREATED)
# async def set_dummy_theme_default():
#     db.set_theme_default()
