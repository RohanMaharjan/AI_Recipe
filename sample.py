import os, random, shutil

# Paths
obj_images = "archive/obj"
test_images = "archive/test"
base = "yolov8/dataset"

# Create folders
for split in ["train/images", "train/labels", "val/images", "val/labels", "test/images", "test/labels"]:
    os.makedirs(os.path.join(base, split), exist_ok=True)

# Split obj into train/val
files = [f for f in os.listdir(obj_images) if f.endswith(".jpg")]
random.shuffle(files)
split_idx = int(0.8 * len(files))

train_files = files[:split_idx]
val_files = files[split_idx:]

def move_files(file_list, split):
    for f in file_list:
        img_src = os.path.join(obj_images, f)
        lbl_src = os.path.join(obj_images, f.replace(".jpg", ".txt"))
        shutil.copy(img_src, os.path.join(base, f"{split}/images", f))
        shutil.copy(lbl_src, os.path.join(base, f"{split}/labels", f.replace(".jpg", ".txt")))

move_files(train_files, "train")
move_files(val_files, "val")

# Move test set
for f in os.listdir(test_images):
    if f.endswith(".jpg"):
        shutil.copy(os.path.join(test_images, f), os.path.join(base, "test/images", f))
        shutil.copy(os.path.join(test_images, f.replace(".jpg", ".txt")), os.path.join(base, "test/labels", f.replace(".jpg", ".txt")))
