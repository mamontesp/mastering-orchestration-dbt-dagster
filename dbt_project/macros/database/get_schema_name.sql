{% macro generate_schema_name(custom_schema_name, node) -%}

    {%- set default_schema = target.schema -%}
    {%- set client_schema = var('client', default_schema) -%}

    {%- if custom_schema_name == 'telephony_sources'-%} 
        {{ custom_schema_name | lower | replace(' ', '_') | replace('.', '') }}
    {%- elif custom_schema_name is not none -%} 
        {{ client_schema | lower | replace(' ', '_') | replace('.', '')}}_{{ custom_schema_name | lower }}
    {%- else -%}
        {{ client_schema | lower | replace(' ', '_') | replace('.', '') }}
    {%- endif -%}
{%- endmacro %}
