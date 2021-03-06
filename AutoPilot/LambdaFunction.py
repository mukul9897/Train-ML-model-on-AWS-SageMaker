import os
import io
import boto3
import json
import csv

# grab environment variables
#ep_name contians endpoint name of our ml model
ep_name = "ENDPOINT_NAME"
import boto3,sys

sm_rt = boto3.Session().client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    data = json.loads(json.dumps(event))
    payload = data['data']
    print(payload)
    response = sm_rt.invoke_endpoint(EndpointName=ep_name, ContentType='text/csv', Accept='text/csv', Body=payload)
    response = response['Body'].read().decode("utf-8")
    return response
