from ultralytics import YOLO
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    'backend',
    'models',
    'best.pt'
)

model = YOLO(MODEL_PATH)

def detect_food(image_path):
    """
    Detect food items from an image
    Returns list of detected ingredient names
    """
    results = model(image_path, conf=0.25)

    detected_items = set()
    for r in results:
        for cls in r.boxes.cls:
            detected_items.add(model.names[int(cls)])

    return list(detected_items)
