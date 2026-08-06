CREATE OR REPLACE TABLE
`retail-data-eng-platform.silver.order_payments`
AS

SELECT

order_id,

SAFE_CAST(payment_sequential AS INT64) AS payment_sequential,

payment_type,

SAFE_CAST(payment_installments AS INT64) AS payment_installments,

SAFE_CAST(payment_value AS NUMERIC) AS payment_value

FROM
`retail-data-eng-platform.bronze.order_payments`;