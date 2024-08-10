import os.path
from uuid import uuid4

from fastapi import UploadFile, HTTPException


class CustomException(HTTPException):
    pass


class FileTooLarge(CustomException):
    pass


class InvalidColor(CustomException):
    pass


def upload_file(file: UploadFile, subfolder: str = "") -> str:
    img_name = None
    if file:
        if file.size > 50 * 1024 * 1024:
            raise FileTooLarge(400, "File must <= 50MiB")
        ext = file.filename.split(".")[-1]
        img_name = f"{uuid4().hex}.{ext}"
        if subfolder:
            img_name = os.path.join('uploads', subfolder, img_name)
        else:
            img_name = os.path.join('uploads', img_name)
        with open(img_name, "wb") as f:
            f.write(file.file.read())
    return img_name


def validate_hex_color(color):
    if len(color) != 7 or color[0] != '#':
        raise InvalidColor(400, 'Invalid color')
    for c in color[1:]:
        if c not in '0123456789abcdef':
            raise InvalidColor(400, 'Invalid color')
    return True
