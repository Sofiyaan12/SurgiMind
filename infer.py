import os
from ultralytics import YOLO

MODEL_PATH = "models/best_v1.pt"
model = YOLO(MODEL_PATH)

def run_inference(input_video: str) -> str:
    model.predict(
        source=input_video,
        conf=0.3,
        save=True,
        project="outputs",
        name="result",
        exist_ok=True
    )

    # return FULL relative path
    filename = os.path.basename(input_video)
    return f"/outputs/result/{filename}"
