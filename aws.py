import boto3

s3=boto3.resource("s3")
bucket=s3.create_bucket(Bucket="vishal18092000", CreateBucketConfiguration={"LocationConstraint":"us-east-2"})
print(bucket)

