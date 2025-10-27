from fastapi import FastAPI, File, UploadFile
from typing import List
import shutil
import os
from code_analysis import init, test
from pydantic import BaseModel
from fastapi.responses import FileResponse
import base64
from fastapi.responses import StreamingResponse

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


class DownloadLinks(BaseModel):
    download_links: list[str]


@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    saved_files = []

    for file in files:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        saved_files.append(file.filename)

    init(saved_files)
    buffers = test(saved_files)

    download_links = [
        f"/download/{os.path.basename(path)}" for path in buffers
    ]
    return {"message": "Files processed successfully!", "download_links": download_links}

    @app.get("/download/{filename}")
    async def download_file(filename: str):
        file_path = os.path.join(OUTPUT_DIR, filename)
        return FileResponse(file_path)
