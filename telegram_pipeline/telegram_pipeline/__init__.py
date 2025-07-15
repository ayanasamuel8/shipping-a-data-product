from dagster import Definitions, load_assets_from_modules

from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)
from .schedules import daily_etl_schedule 
schedules = [daily_etl_schedule]