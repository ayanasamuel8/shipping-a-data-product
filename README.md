# 📊 Telegram Medical Insights

This project builds an end-to-end data pipeline to extract, transform, enrich, and serve analytics on Ethiopian medical business data collected from public Telegram channels. 🚀

## 📝 Overview

The pipeline:

* 📲 Scrapes Telegram channels for messages and images
* 🗃️ Stores raw data in a data lake as JSON files
* 🐘 Loads and transforms data into a PostgreSQL warehouse using dbt
* 🖼️ Enriches data with YOLOv8 object detection on images
* ⚡ Exposes insights through a FastAPI analytical API
* 🕹️ Orchestrates the full workflow using Dagster

## 📂 Project Structure

* `data/` — Raw Telegram data stored under `raw/telegram_messages/`
* `dbt/` — Data transformation and modeling with dbt
* `dags/` — Dagster jobs for pipeline orchestration
* `fastapi_app/` — FastAPI backend serving API endpoints
* `yolo_detection/` — YOLOv8 image detection scripts
* `.env` — Secrets and config variables (keep private!)
* `docker-compose.yml` & `Dockerfile` — Container setup
* `requirements.txt` — Python dependencies

## ⚙️ Setup Instructions

1. 🔄 Clone the repo and `cd` into the project folder
2. 🔑 Create a `.env` file with your Telegram API keys and PostgreSQL credentials
3. 🐳 Run `docker-compose up -d` to start PostgreSQL and related services
4. 📥 Run the Telegram scraper to collect raw data
5. 📊 Load raw data into PostgreSQL and run dbt to build your data warehouse
6. 🖼️ Run YOLOv8 detection scripts to enrich image data
7. 🚀 Start FastAPI server to serve analytical endpoints

## 🛠️ Technologies Used

* Python 3.10 🐍
* PostgreSQL 🐘
* dbt (Data Build Tool) 🏗️
* Telethon (Telegram API) 📱
* YOLOv8 (Ultralytics) 🎯
* FastAPI (API backend) ⚡
* Dagster (Orchestration) 🕹️
* Docker & Docker Compose 🐳

## 🔐 Notes

* Keep your `.env` file secure and never push it to GitHub! 🔒
* The project is modular, scalable, and reproducible 🌱
* Use the API endpoints to answer key business questions about medical products and channel activity 📈