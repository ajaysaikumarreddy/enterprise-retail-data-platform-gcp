"""
Project : Enterprise Retail Data Platform
Purpose : Test Google Cloud Storage Connection
Author  : Ajay Sai Kumar Reddy
"""

from google.cloud import storage


def main():
    # Uses Application Default Credentials (ADC)
    client = storage.Client()

    print("=" * 60)
    print("Connected Successfully to Google Cloud Storage")
    print("=" * 60)

    print("\nBuckets:\n")

    for bucket in client.list_buckets():
        print(bucket.name)


if __name__ == "__main__":
    main()