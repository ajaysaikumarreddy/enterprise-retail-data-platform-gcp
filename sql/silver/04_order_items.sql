CREATE OR REPLACE TABLE
`retail-data-eng-platform.silver.order_items`
AS

SELECT

order_id,

SAFE_CAST(order_item_id AS INT64) AS order_item_id,

product_id,

seller_id,

TIMESTAMP(shipping_limit_date) AS shipping_limit_date,

SAFE_CAST(price AS NUMERIC) AS price,

SAFE_CAST(freight_value AS NUMERIC) AS freight_value

FROM
`retail-data-eng-platform.bronze.order_items`;