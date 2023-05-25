import boto3
from chalice import Chalice
import os

from utils_bucket.create_bucket import create_bucket
from utils_bucket.delete_bucket import delete_bucket
from utils_bucket.download_file_from_bucket import download_file
from utils_bucket.list_buckets import list_buckets
from utils_bucket.upload_file_to_bucket import upload_file

app = Chalice(app_name='Translator')
translate = boto3.client('translate')

@app.lambda_function()
def translate_text(event, context):

    source_language = event['source_language']
    target_language = event['target_language']
    text = event['text']

    translate = boto3.client(
        'translate',
        aws_access_key_id='ACCESS',
        aws_secret_access_key='SECRET',
        region_name='us-east-1'
    )

    response = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_language,
        TargetLanguageCode=target_language
    )

    translated_text = response['TranslatedText']

    create_bucket("History-Bucket")

    file_name = os.path.abspath("utils_bucket/history/history.txt")

    upload_file(file_name, "History-Bucket", "history.txt")

    download_file("history.txt", "History-Bucket", "history.txt")


    return {'translated_text': translated_text}

