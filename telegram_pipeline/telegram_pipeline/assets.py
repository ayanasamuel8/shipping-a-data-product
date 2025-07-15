
from dagster import op
import subprocess
from dagster import In, Nothing


@op
def scrape_telegram_data():
    subprocess.run(["python", "telegram_scraper/scraper.py"], check=True)

@op(ins={"start_after": In(Nothing)})
def load_raw_to_postgres():
    subprocess.run(["python", "loaders/json_to_postgres.py"], check=True)

@op(ins={"start_after": In(Nothing)})
def run_dbt_transformations():
    subprocess.run(["dbt", "run", "--project-dir", "dbt/telegram_dbt"], check=True)

@op(ins={"start_after": In(Nothing)})
def run_yolo_enrichment():
    subprocess.run(["python", "yolo_detection/enrich_images.py"], check=True)