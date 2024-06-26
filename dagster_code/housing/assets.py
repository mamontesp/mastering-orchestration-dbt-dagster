import json
from dagster import OpExecutionContext
from dagster_dbt import dbt_assets, DbtCliResource
from housing.resources import DbtRunResource
from housing.partitions import telephony_providers

from housing.constants import (
    DBT_MANIFEST_PATH
)

def dbt_resource_to_args(command, dbt_run_resource: DbtRunResource, partition_key = '') -> list:
    '''
    Translates DbtRunResource into cli args.
    You can add as many parameters as you like in dbt_run_resource,
    And have it translated to args or vars in this function.
    :param config:
    :return:
    args list
    '''
    args = [command]

    if dbt_run_resource.full_refresh and command in ('run', 'build'):
        args += ["--full-refresh"]

    client = partition_key if dbt_run_resource.client is None else dbt_run_resource.client
    # construct vars dict
    vars_dict = {
        "client": client,
        "start_date": dbt_run_resource.start_date,
        "end_date": dbt_run_resource.end_date
    }

    args += ["--vars", json.dumps(vars_dict)]

    return args

@dbt_assets(manifest=DBT_MANIFEST_PATH, partitions_def=telephony_providers, select="mobile")
def dbt_client_mobile_telephony(context: OpExecutionContext, dbt_run_resource: DbtRunResource, dbt: DbtCliResource):
    """
    dbt models under mobile folder
    """
    partition_key = context.partition_key

    dbt_seed_args = dbt_resource_to_args("seed", dbt_run_resource, partition_key = partition_key)

    yield from dbt.cli(dbt_seed_args, context=context).stream()

    dbt_run_args = dbt_resource_to_args("run", dbt_run_resource, partition_key = partition_key)

    yield from dbt.cli(dbt_run_args, context=context).stream()

@dbt_assets(manifest=DBT_MANIFEST_PATH, partitions_def=telephony_providers, select="fixed")
def dbt_client_fixed_telephony(context: OpExecutionContext, dbt_run_resource: DbtRunResource, dbt: DbtCliResource):
    """
    dbt models under fixed folder
    """
    partition_key = context.partition_key

    dbt_seed_args = dbt_resource_to_args("seed", dbt_run_resource, partition_key = partition_key)

    yield from dbt.cli(dbt_seed_args, context=context).stream()
    
    dbt_run_args = dbt_resource_to_args("run", dbt_run_resource, partition_key = partition_key)

    yield from dbt.cli(dbt_run_args, context=context).stream()
