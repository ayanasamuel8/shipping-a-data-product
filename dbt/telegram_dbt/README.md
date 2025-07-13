
# Telegram Medical Insights — dbt Project

This dbt project is part of the Telegram Medical Insights pipeline. It transforms, models, and documents data scraped from Ethiopian medical Telegram channels and loaded into PostgreSQL.

## Project Structure

- `models/example/` — Example dbt models and schema
- `analyses/`, `macros/`, `seeds/`, `snapshots/`, `tests/` — Standard dbt folders for advanced modeling and testing
- `dbt_project.yml` — Project configuration

## Usage

1. Ensure your PostgreSQL database is running and loaded with raw Telegram data.
2. Configure your dbt profile to connect to the database.
3. Run dbt models:
   - `dbt run` — Build models
   - `dbt test` — Run data quality tests
   - `dbt docs generate` — Generate documentation
   - `dbt docs serve` — View docs in your browser

## Example Models

- `my_first_dbt_model.sql` — Example transformation
- `my_second_dbt_model.sql` — Example transformation
- `schema.yml` — Data quality tests and documentation

## Resources

- [dbt Documentation](https://docs.getdbt.com/docs/introduction)
- [dbt Discourse](https://discourse.getdbt.com/)
- [dbt Community Slack](https://community.getdbt.com/)
