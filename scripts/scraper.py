import os
import json
import asyncio
import logging
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv

load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
SESSION = os.getenv("TELEGRAM_SESSION")

DATA_DIR = "data/raw/telegram_messages"

CHANNELS = [
    "https://t.me/CheMed123",
    "https://t.me/tikvahpharma",
    "https://t.me/lobelia4cosmetics",
    "https://t.me/Thequorachannel"
]


import base64

def make_serializable(obj):
    if isinstance(obj, dict):
        return {k: make_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [make_serializable(v) for v in obj]
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, bytes):
        return base64.b64encode(obj).decode("utf-8")
    else:
        return obj



async def scrape_channel(client, channel_url):
    channel_name = channel_url.split("/")[-1]
    today = datetime.today().strftime("%Y-%m-%d")
    folder_path = os.path.join(DATA_DIR, today, channel_name)
    os.makedirs(folder_path, exist_ok=True)

    messages = []

    async for msg in client.iter_messages(channel_url, limit=10000):
        try:
            msg_dict = make_serializable(msg.to_dict())
            messages.append(msg_dict)

            # Save image if it exists
            if isinstance(msg.media, MessageMediaPhoto):
                img_path = os.path.join(folder_path, f"{msg.id}.jpg")
                await client.download_media(msg.media, file=img_path)

        except Exception as e:
            logging.warning(f"⚠️ Error processing message {msg.id} in {channel_name}: {e}")

    # Save all messages to a JSON file
    json_path = os.path.join(folder_path, "messages.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

    logging.info(f"✅ Scraped {len(messages)} messages from {channel_name}")


async def main():
    async with TelegramClient(SESSION, API_ID, API_HASH) as client:
        for channel in CHANNELS:
            try:
                await scrape_channel(client, channel)
            except Exception as e:
                logging.error(f"❌ Failed scraping {channel}: {e}")


if __name__ == "__main__":
    asyncio.run(main())
