from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import shutil
import os
from infer import run_inference

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
STATIC_DIR = "static"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Serve frontend
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Serve output videos
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.post("/predict/video")
async def predict_video(file: UploadFile = File(...)):
    input_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_video = run_inference(input_path)

    return {
        "message": "Inference complete",
        "output_video": output_video
    }
