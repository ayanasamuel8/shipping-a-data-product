
# 📊 Telegram Medical Insights

An end-to-end data platform for extracting, transforming, enriching, and serving analytics on Ethiopian medical business data from public Telegram channels.

---

## 📝 Project Overview

This project enables:
- Scraping Telegram channels for messages and images (via `scripts/scraper.py`)
- Storing raw data (JSON, images) in `data/raw/telegram_messages/`
- Loading and transforming data into PostgreSQL using dbt (`scripts/json_to_postgres.py`, `dbt/telegram_dbt/`)
- Enriching image data with YOLOv8 object detection (`yolo_detection/`)
- Serving analytics via a FastAPI backend (`fastapi_app/`)
- Orchestrating the workflow with Dagster (`dags/`)

---

## 📂 Project Structure

```
telegram-medical-insights/
├── data/raw/telegram_messages/      # Raw Telegram data (JSON, images)
├── dbt/telegram_dbt/                # dbt project for data modeling
│   ├── models/example/              # Example dbt models
│   ├── analyses/, macros/, seeds/, snapshots/, tests/
├── dags/                            # Dagster orchestration jobs
├── fastapi_app/                     # FastAPI backend for analytics
├── models/marts/                    # Core analytical SQL models
├── scripts/                         # ETL scripts (scraper, loader)
├── yolo_detection/                  # YOLOv8 image detection scripts
├── Dockerfile, docker-compose.yml   # Containerization
├── requirements.txt                 # Python dependencies
├── .env                             # Secrets/config (not committed)
```

---

## ⚙️ Setup & Usage

1. **Clone the repo** and `cd` into the project folder
2. **Create a `.env` file** with your Telegram API keys and PostgreSQL credentials
3. **Start services:**
   - `docker-compose up -d` (PostgreSQL, etc.)
4. **Scrape Telegram data:**
   - `python scripts/scraper.py` (collects messages & images)
5. **Load data into PostgreSQL:**
   - `python scripts/json_to_postgres.py`
6. **Run dbt transformations:**
   - `cd dbt/telegram_dbt`
   - `dbt run` (builds models)
   - `dbt test` (runs data quality tests)
   - `dbt docs generate && dbt docs serve` (view model docs/lineage)
7. **Enrich images with YOLOv8:**
   - See `yolo_detection/` for scripts and instructions
8. **Start FastAPI analytics server:**
   - See `fastapi_app/` for API endpoints
9. **Orchestrate with Dagster:**
   - See `dags/` for pipeline automation

---

## 🛠️ Technologies Used

- Python 3.10
- PostgreSQL
- dbt (Data Build Tool)
- Telethon (Telegram API)
- YOLOv8 (Ultralytics)
- FastAPI (API backend)
- Dagster (Orchestration)
- Docker & Docker Compose

---

## � Visuals & Analytics

- **Bar Chart:** Top 10 most mentioned medical products (see `notebooks/`)
- **Pie Chart:** Distribution of media types (text vs. images)
- **dbt Docs:** Interactive model lineage and documentation

---

## 🔐 Notes

- Keep your `.env` file secure and never push it to GitHub!
- The project is modular, scalable, and reproducible
- Use the API endpoints to answer key business questions about medical products and channel activity