CREATE OR REPLACE TABLE
`retail-data-eng-platform.silver.sellers`
AS

SELECT

seller_id,

SAFE_CAST(seller_zip_code_prefix AS INT64) AS seller_zip_code_prefix,

INITCAP(TRIM(seller_city)) AS seller_city,

UPPER(TRIM(seller_state)) AS seller_state

FROM
`retail-data-eng-platform.bronze.sellers`;