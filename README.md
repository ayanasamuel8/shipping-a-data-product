

# 📊 Telegram Medical Insights

An end-to-end, modular data platform for extracting, transforming, enriching, and serving analytics on Ethiopian medical business data from public Telegram channels.

---

## 📝 Project Overview

This project enables:
- **Scraping** Telegram channels for messages and images (`scripts/scraper.py`)
- **Storing** raw data (JSON, images) in `data/raw/telegram_messages/`
- **Loading & transforming** data into PostgreSQL using dbt (`scripts/json_to_postgres.py`, `dbt/telegram_dbt/`)
- **Enriching** image data with YOLOv8 object detection (`yolo_detection/`)
- **Serving analytics** via a FastAPI backend (`fastapi_app/`)
- **Orchestrating** the workflow with Dagster (`dags/`)
- **Exploring & visualizing** data in Jupyter notebooks (`notebooks/`)

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
├── models/marts/                    # Core analytical SQL models (star schema)
├── scripts/                         # ETL scripts (scraper, loader)
├── yolo_detection/                  # YOLOv8 image detection scripts
├── notebooks/                       # Data exploration & visualization
├── telegram_pipeline/               # Python package for pipeline assets
├── Dockerfile, docker-compose.yml   # Containerization
├── requirements.txt                 # Python dependencies
├── .env                             # Secrets/config (not committed)
```

---

## ⚙️ Setup & Usage

### 1. Clone & Configure

```bash
git clone https://github.com/ayanasamuel8.git
cd telegram-medical-insights
```

Create a `.env` file with your Telegram API keys and PostgreSQL credentials:

```
TELEGRAM_API_ID=...
TELEGRAM_API_HASH=...
TELEGRAM_SESSION=...
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=telegram_data
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 2. Start Services

```bash
docker-compose up -d
```
This starts PostgreSQL and any other defined services.

### 3. Scrape Telegram Data

```bash
python scripts/scraper.py
```
Collects messages and images from configured Telegram channels.

### 4. Load Data into PostgreSQL

```bash
python scripts/json_to_postgres.py
```
Loads raw JSON messages into the `raw.telegram_messages` table.

### 5. Run dbt Transformations

```bash
cd dbt/telegram_dbt
dbt run           # Build models (staging, fact, dimension)
dbt test          # Run data quality tests
dbt docs generate # Generate documentation
dbt docs serve    # View docs/lineage in browser
```
Models are defined in `models/` and `models/marts/` (star schema: fact & dimension tables).

### 6. Enrich Images with YOLOv8

See `yolo_detection/` for scripts and instructions to run object detection on images. Detected objects can be used to enrich analytics.

### 7. Start FastAPI Analytics Server

See `fastapi_app/` for API endpoints and instructions to launch the analytics backend.

### 8. Orchestrate with Dagster

See `dags/` for pipeline automation and orchestration jobs.

### 9. Explore & Visualize Data

Use Jupyter notebooks in `notebooks/` for:
- Bar chart: Top 10 most mentioned medical products
- Pie chart: Distribution of media types (text vs. images)
- Custom analytics and EDA

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
- Jupyter (Visualization/EDA)

---

## 📊 Visuals & Analytics

- **Bar Chart:** Top 10 most mentioned medical products (see `notebooks/`)
- **Pie Chart:** Distribution of media types (text vs. images)
- **dbt Docs:** Interactive model lineage and documentation

---

## 🔐 Notes

- Keep your `.env` file secure and never push it to GitHub!
- The project is modular, scalable, and reproducible
- Use the API endpoints to answer key business questions about medical products and channel activity
