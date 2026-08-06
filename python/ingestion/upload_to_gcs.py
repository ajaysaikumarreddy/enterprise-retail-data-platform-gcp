"""
Project : Enterprise Retail Data Platform
Purpose : Upload files to Google Cloud Storage
Author  : Ajay Sai Kumar Reddy
"""

from pathlib import Path
from google.cloud import storage

BUCKET_NAME = "retail-data-eng-platform-landing"
LOCAL_FOLDER = Path("datasets/source")
DESTINATION_PREFIX = "landing/olist/"


def upload_folder():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    for file_path in LOCAL_FOLDER.glob("*.csv"):
        blob = bucket.blob(f"{DESTINATION_PREFIX}{file_path.name}")
        blob.upload_from_filename(file_path)

        print(f"Uploaded: {file_path.name}")


if __name__ == "__main__":
    upload_folder()