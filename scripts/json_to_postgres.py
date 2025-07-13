import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
)

cur = conn.cursor()

cur.execute("""
    CREATE SCHEMA IF NOT EXISTS raw;
    CREATE TABLE IF NOT EXISTS raw.telegram_messages (
        id BIGINT PRIMARY KEY,
        date TIMESTAMPTZ,
        message TEXT,
        from_id TEXT,
        channel TEXT,
        has_photo BOOLEAN,
        raw_json JSONB
    );
""")
conn.commit()

def load_messages_from_folder(folder_path, channel):
    count = 0
    for root, _, files in os.walk(folder_path):
        for f in files:
            if f == "messages.json":
                with open(os.path.join(root, f), encoding="utf-8") as infile:
                    messages = json.load(infile)
                    for msg in messages:
                        try:
                            # Safely extract from_id user_id if it exists
                            from_id_obj = msg.get("from_id")
                            if isinstance(from_id_obj, dict):
                                from_id = from_id_obj.get("user_id")
                            else:
                                from_id = None

                            cur.execute("""
                                INSERT INTO raw.telegram_messages (id, date, message, from_id, channel, has_photo, raw_json)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)
                                ON CONFLICT (id) DO NOTHING;
                            """, (
                                msg.get("id"),
                                msg.get("date"),
                                msg.get("message"),
                                str(from_id) if from_id is not None else None,
                                channel,
                                msg.get("media") is not None,
                                json.dumps(msg),
                            ))
                            count += 1
                        except Exception as e:
                            print(f"⚠️ Skipping message due to error: {e}")
    conn.commit()
    print(f"✅ Loaded {count} messages from {folder_path}")

if __name__ == "__main__":
    base_dir = "data/raw/telegram_messages"
    for date_folder in os.listdir(base_dir):
        for channel in os.listdir(os.path.join(base_dir, date_folder)):
            path = os.path.join(base_dir, date_folder, channel)
            print(f"Loading {channel} from {date_folder}...")
            load_messages_from_folder(path, channel)
