import os
import psycopg2
from dotenv import load_dotenv
from ultralytics import YOLO
from PIL import Image
from pathlib import Path
import json

load_dotenv()

# Load model
model = YOLO("yolov8n.pt")  # Small model, good for fast inference

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
)
cur = conn.cursor()

# Create detection table
cur.execute("""
CREATE SCHEMA IF NOT EXISTS analytics;
CREATE TABLE IF NOT EXISTS analytics.fct_image_detections (
    id SERIAL PRIMARY KEY,
    message_id BIGINT,
    object_class TEXT,
    confidence NUMERIC,
    FOREIGN KEY (message_id) REFERENCES analytics.fct_messages(message_id)
);
""")
conn.commit()

def detect_objects_on_images(base_dir="data/raw/telegram_messages"):
    for date_folder in Path(base_dir).iterdir():
        for channel_folder in date_folder.iterdir():
            for file in channel_folder.iterdir():
                if file.suffix == ".jpg":
                    try:
                        message_id = int(file.stem)
                        results = model(str(file))  # Run detection

                        for r in results:
                            boxes = r.boxes
                            for box in boxes:
                                cls_id = int(box.cls[0])
                                conf = float(box.conf[0])
                                class_name = model.names[cls_id]

                                # Insert into database
                                cur.execute("""
                                    INSERT INTO analytics.fct_image_detections (message_id, object_class, confidence)
                                    VALUES (%s, %s, %s)
                                """, (message_id, class_name, conf))

                        print(f"✅ Detected objects in image {file.name}")
                    except Exception as e:
                        print(f"⚠️ Skipped {file.name}: {e}")
    conn.commit()

if __name__ == "__main__":
    detect_objects_on_images()