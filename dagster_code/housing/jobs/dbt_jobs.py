from dagster import define_asset_job, AssetSelection, partitioned_config
from housing.partitions import telephony_providers
from housing.assets import (
    dbt_client_fixed_telephony,
    dbt_client_mobile_telephony
)

from housing.constants import DBT_ASSET_CONCURRENCY

@partitioned_config(partitions_def=telephony_providers)
def dbt_housing_client_config(partition_key: str):

    return {
        "resources": {
            "dbt_run_resource": {
                "config": {
                    "client": partition_key,
                    "full_refresh": False
                }
            }
        },
        "execution": {
            "config": {
                "multiprocess": {
                    "max_concurrent": DBT_ASSET_CONCURRENCY,  # limits concurrent assets to this constant
                }
            }
        }
    }


run_fixed_telephony_job = define_asset_job("run_fixed_telephony_job",
                               config=dbt_housing_client_config,
                               partitions_def=telephony_providers,
                               selection=AssetSelection.assets(dbt_client_fixed_telephony),
                               tags={
                                   'database': 'duckdb'
                               }
                               )

run_mobile_telephony_job = define_asset_job("run_mobile_telephony_job",
                               config=dbt_housing_client_config,
                               partitions_def=telephony_providers,
                               selection=AssetSelection.assets(dbt_client_mobile_telephony),
                               tags={
                                   'database': 'duckdb'
                               }
                               )