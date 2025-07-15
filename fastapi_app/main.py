from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi_app.database import SessionLocal
import fastapi_app.crud as crud
import fastapi_app.schemas as schemas
from typing import List

app = FastAPI(title="Telegram Medical Analytics API")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Telegram Medical Analytics API"}
@app.get("/api/reports/top-products", response_model=List[schemas.ProductFrequency])
def read_top_products(limit: int = 10, db: Session = Depends(get_db)):
    results = crud.get_top_products(db, limit)
    return [{"product": r[0], "count": r[1]} for r in results]


@app.get("/api/channels/{channel_name}/activity", response_model=List[schemas.ChannelActivity])
def read_channel_activity(channel_name: str, db: Session = Depends(get_db)):
    results = crud.get_channel_activity(db, channel_name)
    return [{"date": r[0].strftime("%Y-%m-%d"), "message_count": r[1]} for r in results]


@app.get("/api/search/messages", response_model=List[schemas.SearchResult])
def search_telegram_messages(query: str, db: Session = Depends(get_db)):
    results = crud.search_messages(db, query)
    return [{"message_id": r[0], "message": r[1], "channel": r[2]} for r in results]