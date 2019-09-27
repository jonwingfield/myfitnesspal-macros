#!/bin/bash

echo '-- Creating zipfile with code'

role_name="arn:aws:iam::181060896241:role/service-role/myFitnessPalMacros-role-laxz2ov1"
function_name="myFitnessPalMacros"

rm $function_name.zip;  zip -r $function_name.zip ./*

aws lambda create-function \
  --function-name $function_name \
  --runtime "python3.7" \
  --role $role_name \
  --handler handler.aws_event_handler \
  --timeout 10 \
  --memory-size 128 \
  --zip-file fileb://$(pwd)/$function_name.zip \
  --description "Gets macros from My Fitness Pal" \
  --region us-east-1
