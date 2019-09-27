#!/bin/bash

function_name="myFitnessPalMacros"

echo '-- Creating zipfile with code'
rm $function_name.zip;  zip -r $function_name.zip ./*

echo '-- Updating lambda function on AWS (usually takes a few seconds'
aws lambda update-function-code \
  --function-name $function_name \
  --zip-file fileb://$(pwd)/$function_name.zip \
  --region us-east-1
