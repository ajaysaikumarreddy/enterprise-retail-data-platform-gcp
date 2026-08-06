"""
------------------------------------------------------------
Project : Enterprise Retail Data Platform
Author  : Ajay Sai Kumar Reddy
Purpose : Load all CSV files from GCS into BigQuery Bronze
------------------------------------------------------------
"""

from google.cloud import bigquery
from python.utilities.audit import log_ingestion
from config.settings import (
    PROJECT_ID,
    BUCKET_NAME,
    BRONZE_DATASET,
    LANDING_FOLDER,
)

from config.gcp_clients import (
    get_storage_client,
    get_bigquery_client,
)


def load_csv_files():
    """
    Loads all CSV files from the configured GCS landing folder
    into the Bronze BigQuery dataset.
    """

    storage_client = get_storage_client()
    bigquery_client = get_bigquery_client()

    bucket = storage_client.bucket(BUCKET_NAME)

    blobs = bucket.list_blobs(prefix=LANDING_FOLDER)

    print("=" * 70)
    print("Loading CSV Files into BigQuery Bronze")
    print("=" * 70)

    for blob in blobs:

        # Skip non-CSV files
        if not blob.name.endswith(".csv"):
            continue

        # Example:
        # landing/csv/customers.csv
        file_name = blob.name.split("/")[-1]

        # customers
        table_name = file_name.replace(".csv", "")

        table_id = (
            f"{PROJECT_ID}.{BRONZE_DATASET}.{table_name}"
        )

        source_uri = f"gs://{BUCKET_NAME}/{blob.name}"

        print(f"\nLoading : {file_name}")

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=True,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        )

        load_job = bigquery_client.load_table_from_uri(
            source_uri,
            table_id,
            job_config=job_config,
        )

        load_job.result()

        table = bigquery_client.get_table(table_id)

        log_ingestion(
            source_name="olist",
            source_file=file_name,
            destination_table=table.table_id,
            rows_loaded=table.num_rows,
            status="SUCCESS"
            )

        print("SUCCESS")
        print(f"Source File : {file_name}")
        print(f"Table       : {table.table_id}")
        print(f"Rows        : {table.num_rows:,}")
        print(f"Columns     : {len(table.schema)}")
        print("-" * 70)

    print("\n")
    print("=" * 70)
    print("All CSV Files Successfully Loaded")
    print("=" * 70)


def main():
    load_csv_files()


if __name__ == "__main__":
    main()