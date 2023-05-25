# API Translator

  localstack start

  chalice-local new-project
  
  [*] Lambda function only
  
  Change app.py to our app.py
  
  chalice-local deploy

  awslocal lambda invoke --function-name {FUNCTION_NAME_AWS_LOCAL} outfile.txt --cli-binary-format raw-in-base64-out --payload file://input.json
  
  cat outfile.txt
  
  cat .\input.json | chalice-local invoke -n translate_text
  
