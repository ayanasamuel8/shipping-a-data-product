# Marts Models — Telegram Medical Insights

This folder contains the core analytical models (marts) for the Telegram Medical Insights project. These models are built on top of the staging layer and are designed for business analysis and reporting.

## Contents

- `stg_telegram_messages.sql` — Staging model that cleans and standardizes raw Telegram message data.
- `fct_messages.sql` — Fact table with message-level analytics (e.g., message length, media flags).
- `dim_channels.sql` — Dimension table listing unique Telegram channels.
- `dim_dates.sql` — Dimension table extracting date parts (weekday, month, year, etc.).
- `schema.yml` — Data quality tests and documentation for marts models.

## Purpose

These models implement a star schema to support:
- Product and channel analytics
- Trend analysis (daily/weekly)
- Media content analysis

All models are designed for efficient querying and integration with BI tools or APIs.
