import os
from PIL import Image

# ===== CONFIG =====
SOURCE_DIR = "assets/"
OUTPUT_DIR = "assets_we"
QUALITY = 80          # 0–100 (75–85 ideal for web)
MAX_WIDTH = 1600      # Resize for performance (set None to keep original)
MAX_HEIGHT = 1600
# ==================

def ensure_output_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def convert_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            original_size = os.path.getsize(input_path)

            # Convert to RGB if image has alpha
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGBA")

            # Resize if needed
            if MAX_WIDTH and MAX_HEIGHT:
                img.thumbnail((MAX_WIDTH, MAX_HEIGHT))

            img.save(
                output_path,
                "WEBP",
                quality=QUALITY,
                method=6  # Best compression
            )

            new_size = os.path.getsize(output_path)
            reduction = ((original_size - new_size) / original_size) * 100

            print(f"✔ {os.path.basename(input_path)}")
            print(f"   {original_size/1024:.1f}KB → {new_size/1024:.1f}KB "
                  f"({reduction:.1f}% smaller)\n")

    except Exception as e:
        print(f"✖ Error processing {input_path}: {e}")

def main():
    ensure_output_dir(OUTPUT_DIR)

    for filename in os.listdir(SOURCE_DIR):
        if filename.lower().endswith(".jpg"):
            input_path = os.path.join(SOURCE_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            convert_image(input_path, output_path)

if __name__ == "__main__":
    main()
