from dagster import job
from telegram_pipeline.assets import (
    scrape_telegram_data,
    load_raw_to_postgres,
    run_dbt_transformations,
    run_yolo_enrichment,
)

@job
def telegram_etl_job():
    data = scrape_telegram_data()
    loaded = load_raw_to_postgres(start_after=data)
    transformed = run_dbt_transformations(start_after=loaded)
    run_yolo_enrichment(start_after=transformed)