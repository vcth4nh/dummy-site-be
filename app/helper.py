from uuid import uuid4

from fastapi import UploadFile


class FileTooLarge(Exception):
    pass


def upload_file(file: UploadFile):
    img_name = None
    if file:
        if file.size > 50 * 1024 * 1024:
            raise FileTooLarge("File must <= 50MiB")
        ext = file.filename.split(".")[-1]
        img_name = f"{uuid4().hex}.{ext}"
        with open(f"uploads/{img_name}", "wb") as f:
            f.write(file.file.read())
    return img_name
