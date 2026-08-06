from google.cloud import storage
from google.cloud import bigquery


def get_storage_client():
    return storage.Client()


def get_bigquery_client():
    return bigquery.Client()