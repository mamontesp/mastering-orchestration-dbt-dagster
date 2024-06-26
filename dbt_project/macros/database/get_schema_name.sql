{% macro generate_schema_name(custom_schema_name, node) -%}

    {%- set default_schema = target.schema -%}
    {%- set client_schema = var('client', default_schema) -%}

    {%- if custom_schema_name == 'telephony_sources'-%} 
        {{ custom_schema_name }}
    {%- elif custom_schema_name is not none -%} 
        {{ client_schema }}_{{ custom_schema_name }}
    {%- else -%}
        {{ client_schema }}
    {%- endif -%}
{%- endmacro %}
