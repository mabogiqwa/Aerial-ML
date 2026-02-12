#Converts labelling dataset to YOLO format
import os
from PIL import Image

# Map class names to IDs
class_map = {
    "small-vehicle": 0,
    "large-vehicle": 1,
    "ship": 2,
    "plane": 3,
    "harbor": 4
}

# Paths for train
input_dir_train = r"C:\Users\name-of-user\folder-name\project-name\dataset\labels\train"
output_dir_train = r"C:\Users\name-of-user\folder-name\project-name\dataset\labels_yolo\train"
image_dir_train = r"C:\Users\name-of-user\folder-name\project-name\dataset\images\train"
os.makedirs(output_dir_train, exist_ok=True)

# Paths for val
input_dir_val = r"C:\Users\name-of-user\folder-name\project-name\dataset\labels\val"
output_dir_val = r"C:\Users\name-of-user\folder-name\project-name\dataset\labels_yolo\val"
image_dir_val = r"C:\Users\name-of-user\folder-name\project-name\dataset\images\val"
os.makedirs(output_dir_val, exist_ok=True)

# Supported image extensions
image_exts = ['.jpg', '.jpeg', '.png']

def convert_labels(input_dir, output_dir, image_dir):
    for filename in os.listdir(input_dir):
        if not filename.endswith(".txt"):
            continue

        in_path = os.path.join(input_dir, filename)
        out_path = os.path.join(output_dir, filename)

        img_name = None
        for ext in image_exts:
            temp_name = filename.replace(".txt", ext)
            temp_path = os.path.join(image_dir, temp_name)
            if os.path.exists(temp_path):
                img_name = temp_name
                break
        if img_name is None:
            print(f"Warning: Image for {filename} not found in {image_dir}!")
            continue
        img_path = os.path.join(image_dir, img_name)

        img_w, img_h = Image.open(img_path).size

        with open(in_path, "r") as f:
            lines = f.readlines()

        yolo_lines = []
        for line in lines:
            if line.startswith("imagesource") or line.startswith("gsd") or line.strip() == "":
                continue

            parts = line.strip().split()
            class_name = parts[-2]
            if class_name not in class_map:
                continue

            coords = list(map(float, parts[:8]))
            xs = coords[0::2]
            ys = coords[1::2]
            xmin, xmax = min(xs), max(xs)
            ymin, ymax = min(ys), max(ys)

            cx = (xmin + xmax) / 2 / img_w
            cy = (ymin + ymax) / 2 / img_h
            w  = (xmax - xmin) / img_w
            h  = (ymax - ymin) / img_h

            yolo_lines.append(f"{class_map[class_name]} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}\n")

        with open(out_path, "w") as f:
            f.writelines(yolo_lines)

    print("Conversion complete")

# Convert both train and val sets
convert_labels(input_dir_train, output_dir_train, image_dir_train)
convert_labels(input_dir_val, output_dir_val, image_dir_val)

