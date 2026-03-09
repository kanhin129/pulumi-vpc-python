from vpc import public_subnet
from security import sg
from ec2 import create_ec2
import pulumi_aws as aws

# 建立 Key Pair（如果你還沒在 AWS 建立過）
key_pair = aws.ec2.KeyPair(
    "basic-key",
    public_key=open("/Users/james/.ssh/linha_id_rsa.pub").read()
)

# 建立 EC2
ec21 = create_ec2(public_subnet, sg, key_pair.key_name, instance_name="basic-ec2-1")

# ec22 = create_ec2(public_subnet, sg, key_pair_name, instance_name="basic-ec2-2")
