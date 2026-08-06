CREATE TABLE IF NOT EXISTS `retail-data-eng-platform.audit.ingestion_log`
(
    run_id STRING,
    source_name STRING,
    source_file STRING,
    destination_table STRING,
    load_time TIMESTAMP,
    rows_loaded INT64,
    status STRING,
    error_message STRING
);