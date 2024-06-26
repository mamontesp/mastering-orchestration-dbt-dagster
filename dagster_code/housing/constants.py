from dagster import file_relative_path
from pathlib import Path
from dagster_dbt import DbtCliResource
import os

#dbt setup
DBT_PROJECT_PATH = file_relative_path(__file__, '../../')
DBT_PROFILES_PATH = Path(DBT_PROJECT_PATH, 'dbt_project', '.dbt')

dbt = DbtCliResource(project_dir=os.fspath(DBT_PROJECT_PATH),profiles_dir=DBT_PROFILES_PATH)
dbt_parse_invocation = dbt.cli(["parse"], manifest={}).wait()
DBT_MANIFEST_PATH = dbt_parse_invocation.target_path.joinpath("manifest.json")
DBT_ASSET_CONCURRENCY = 2