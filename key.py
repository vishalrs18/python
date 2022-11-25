import boto3
key=boto3.client("key_pair","ap-northeast-1")
response = key.create_key_pair(
    KeyName='string',
    DryRun=True|False,
    KeyType='rsa'|'ed25519',
    TagSpecifications=[
        {
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    KeyFormat='pem'|'ppk'
)
print(response)
