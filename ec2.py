import boto3

ec2=boto3.client("ec2",'ap-northeast-1')
key=ec2.create_key_pair(KeyName="mine")
instances=ec2.run_instances(ImageId="ami-099772c3838a3bec1",
                            #InstanceType="t2.micro",
                            MinCount=1,
                            MaxCount=1)
