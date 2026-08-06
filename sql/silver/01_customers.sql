CREATE OR REPLACE TABLE
`retail-data-eng-platform.silver.customers`
AS

SELECT

customer_id,

customer_unique_id,

SAFE_CAST(customer_zip_code_prefix AS INT64) AS customer_zip_code_prefix,

INITCAP(TRIM(customer_city)) AS customer_city,

UPPER(TRIM(customer_state)) AS customer_state

FROM
`retail-data-eng-platform.bronze.customers`;