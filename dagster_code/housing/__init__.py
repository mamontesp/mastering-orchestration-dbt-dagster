from dagster import Definitions, load_assets_from_modules

from . import assets
from .resources import resources
from .jobs import (
    run_mobile_telephony_job
    , run_fixed_telephony_job
)

all_jobs = [
    # dbt jobs
    run_mobile_telephony_job
    , run_fixed_telephony_job
]

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets = all_assets,
    resources = resources,
    jobs= all_jobs
)
