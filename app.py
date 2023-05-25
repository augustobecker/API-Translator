import boto3
from chalice import Chalice

app = Chalice(app_name='Translator')
translate = boto3.client('translate-text')

@app.lambda_function()
def translate_text(event, context):

    source_language = event['source_language']
    target_language = event['target_language']
    text = event['text']

    translate = boto3.client(
        'translate',
        aws_access_key_id='AWS_ACCESS_KEY',
        aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
        region_name='us-east-1'
    )

    response = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_language,
        TargetLanguageCode=target_language
    )

    translated_text = response['TranslatedText']
    return {'translated_text': translated_text}
