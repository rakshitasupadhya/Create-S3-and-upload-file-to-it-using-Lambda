import json
import boto3

def lambda_handler(event, context):
    
    s3=boto3.client('s3')
    buckname="createnewanduploadfile"
    try:
        s3.create_bucket(Bucket=buckname)
        
    except ClientError as e:
        print("Choose difefrent bucket name")
        
    transaction={}
    transaction['transid']='123'
    transaction['type']='PURCHASE'
    transaction['amount']='30'
    transaction['customerid']='CID-111'
    fileName= 'CID-111' + '.json'

    uploadByteStream= bytes(json.dumps(transaction).encode('UTF-8'))
    s3.put_object(Bucket=buckname, Key= fileName, Body=uploadByteStream)
    print('Put completed')
