from dagster import ScheduleDefinition
from telegram_pipeline.jobs.job import telegram_etl_job

daily_etl_schedule = ScheduleDefinition(
    job=telegram_etl_job,
    cron_schedule="0 6 * * *",  # Every day at 6 AM
    name="daily_telegram_etl",
)