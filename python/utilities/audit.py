from datetime import datetime
import uuid

from config.gcp_clients import get_bigquery_client
from config.settings import PROJECT_ID


def log_ingestion(
    source_name,
    source_file,
    destination_table,
    rows_loaded,
    status,
    error_message=None,
):

    client = get_bigquery_client()

    table_id = f"{PROJECT_ID}.audit.ingestion_log"

    rows = [
        {
            "run_id": str(uuid.uuid4()),
            "source_name": source_name,
            "source_file": source_file,
            "destination_table": destination_table,
            "load_time": datetime.utcnow().isoformat(),
            "rows_loaded": rows_loaded,
            "status": status,
            "error_message": error_message,
        }
    ]

    errors = client.insert_rows_json(table_id, rows)

    if errors:
    print("=" * 70)
    print("AUDIT INSERT FAILED")
    print(errors)
    print("=" * 70)
else:
    print("Audit record inserted successfully.")