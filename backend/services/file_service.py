import os
import shutil
from pathlib import Path

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

def save_file(file):

    filepath = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        filepath,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return filepath

def save_file(file):

    filepath = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        filepath,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return filepath

def delete_file(filename):

    upload_root = Path(UPLOAD_DIR).resolve()

    filepath = (
        upload_root / filename
    ).resolve()

    if upload_root not in filepath.parents:
        raise ValueError(
            "Invalid filename"
        )

    if not filepath.exists() or not filepath.is_file():
        return False

    filepath.unlink()

    return True