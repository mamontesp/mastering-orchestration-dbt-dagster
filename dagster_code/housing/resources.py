from dagster import ConfigurableResource
from dagster_dbt import DbtCliResource
from typing import Optional
from housing.constants import DBT_PROJECT_PATH, DBT_PROFILES_PATH

class DbtRunResource(ConfigurableResource):
    '''
    This class is for having custom run attributes passed into the job.
    The items here will be mapped into dbt variables that are passed into invocations.

    This is separate from DbtCliResource, which we declare global dbt config
    Such as project_dir and profiles_dir and are generally static
    '''
    client: Optional[str]
    full_refresh: Optional[bool]
    start_date: Optional[str]
    end_date: Optional[str]

class ClientOptionsResource(ConfigurableResource):
    """
    Optional arguments to be passed with client resource for various jobs.
    """
    full_rebuild: Optional[bool]

class ClientResource(ConfigurableResource):
    """
    Resource to be used for all client level jobs and used in conjunction with dynamic partitions.
    These jobs typically have 1 run per client partition.
    """
    client: str
    options: Optional[ClientOptionsResource]
    dbt_run_resource: Optional[DbtRunResource]


resources = {
    'dbt': DbtCliResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES_PATH,
        global_config_flags=['--cache-selected-only']
    ),
    'dbt_run_resource': DbtRunResource.configure_at_launch(),
    'client_options_resource': ClientOptionsResource.configure_at_launch(),
    'client_resource': ClientResource.configure_at_launch(),
}
