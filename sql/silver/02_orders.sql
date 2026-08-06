CREATE OR REPLACE TABLE
`retail-data-eng-platform.silver.orders`
AS

SELECT

order_id,

customer_id,

UPPER(TRIM(order_status)) AS order_status,

TIMESTAMP(order_purchase_timestamp) AS order_purchase_timestamp,

TIMESTAMP(order_approved_at) AS order_approved_at,

TIMESTAMP(order_delivered_carrier_date) AS order_delivered_carrier_date,

TIMESTAMP(order_delivered_customer_date) AS order_delivered_customer_date,

TIMESTAMP(order_estimated_delivery_date) AS order_estimated_delivery_date

FROM
`retail-data-eng-platform.bronze.orders`;