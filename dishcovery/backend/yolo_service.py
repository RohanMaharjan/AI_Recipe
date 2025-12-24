'''from ultralytics import YOLO
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
'''
from ultralytics import YOLO
import os
from django.conf import settings

# --------------------------------------------------
# Load YOLO model once
# --------------------------------------------------

MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    'backend',
    'models',
    'best.pt'
)

model = YOLO(MODEL_PATH)

# --------------------------------------------------
# Detection function
# --------------------------------------------------

def detect_food(image_path, conf_threshold=0.25):
    """
    Detect food items from an image.

    Args:
        image_path (str): Path to image file
        conf_threshold (float): Confidence threshold

    Returns:
        list[str]: Detected YOLO class names (unchanged)
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    results = model(image_path, conf=conf_threshold)

    detected_items = set()

    for result in results:
        if result.boxes is None:
            continue

        for cls_id in result.boxes.cls:
            label = model.names[int(cls_id)]
            detected_items.add(label)

    return list(detected_items)
