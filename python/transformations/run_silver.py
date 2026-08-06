from pathlib import Path
from google.cloud import bigquery

client = bigquery.Client()

SQL_FOLDER = Path("sql/silver")


def run_sql(file_path):
    print("=" * 70)
    print(f"Running {file_path.name}")
    print("=" * 70)

    query = file_path.read_text(encoding="utf-8")

    job = client.query(query)
    job.result()

    print("SUCCESS\n")


def main():

    sql_files = sorted(SQL_FOLDER.glob("*.sql"))

    for file in sql_files:
        run_sql(file)

    print("=" * 70)
    print("All Silver Transformations Completed")
    print("=" * 70)


if __name__ == "__main__":
    main()