from google.cloud import storage


def get_storage_client(credentials_json):
    storage_client = storage.Client.from_service_account_json(json_credentials_path=credentials_json)
    return storage_client


def upload_blob(credentials_json, bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # credentials_json = "credentials-json-name"
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = get_storage_client(credentials_json)
    if storage_client is None:
        print(f'upload_blob: Failed to get storage client for service account {credentials_json}.')
        return False

    bucket = storage_client.bucket(bucket_name)
    if bucket is None:
        print(f'upload_blob: Failed to get bucket {bucket_name}')
        return False

    blob = bucket.blob(destination_blob_name)
    if blob is None:
        print(f'upload_blob: Failed to get blob {destination_blob_name}')
        return False

    blob.upload_from_filename(source_file_name)

    print(
        "upload_blob: Uploaded file {} to {} as {}".format(
            source_file_name, bucket_name, destination_blob_name
        )
    )

    return True

