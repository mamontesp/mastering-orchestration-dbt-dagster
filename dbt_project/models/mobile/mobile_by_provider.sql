SELECT
    AÑO as year
    , TRIMESTRE as trimester
    , PROVEEDOR as provider
    , "LINEAS EN SERVICIO" as lines_in_service
    , "LINEAS PREPAGO" as prepaid_lines
    , "LINEAS POSPAGO" as postpaid_lines
    , "LINEAS ACTIVADAS" as enabled_lines
    , "LINEAS RETIRADAS" as retired_lines
FROM {{ ref('mobile_phone_subscribers_by_category') }} 
WHERE PROVEEDOR = '{{ var("client") }}'
