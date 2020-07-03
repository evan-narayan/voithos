""" Download and upload files to AWS S3 """
import boto3
from tqdm import tqdm

import voithos.lib.aws.aws as aws


def callback(progress_bar):
    """ Progress callback for s3 operations """

    def inner(bytes_amount):
        progress_bar.update(bytes_amount)

    return inner


def download(path, bucket_name, key, print_progress=True):
    """ Download file named key from bucket bucket_name to path """
    s3client = aws.get_client("s3")
    if not print_progress:
        s3client.download_file(bucket_name, key, path)
    file_object = boto3.resource("s3").Object(bucket_name, key)
    filesize = file_object.content_length
    with tqdm(total=filesize, unit="B", unit_scale=True, desc=key) as progress_bar:
        s3client.download_file(bucket_name, key, path, Callback=callback(progress_bar))


def upload(path, bucket_name, key):
    """ Upload file at path to bucket bucket_name named key """
    s3client = aws.get_client("s3")
    s3client.upload_file(bucket_name, key, path)
