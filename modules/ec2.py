# modules/ec2.py

import pulumi
import pulumi_aws as aws
from config.config import instance_name, instance_type, public_key_path, keypair_name


def create_ec2(subnet, sg):

    # 讀取 SSH public key
    with open(public_key_path) as f:
        public_key = f.read().strip()

    key_pair = aws.ec2.KeyPair(
        "ec2-keypair",
        key_name=keypair_name,
        public_key=public_key,
    )

    # 取得 AMI
    ami = aws.ec2.get_ami(
        most_recent=True,
        owners=["amazon"],
        filters=[
            {
                "name": "name",
                "values": ["amzn2-ami-hvm-*-x86_64-gp2"],
            }
        ],
    )

    # EC2
    ec2 = aws.ec2.Instance(
        instance_name,
        instance_type=instance_type,
        ami=ami.id,
        subnet_id=subnet.id,
        vpc_security_group_ids=[sg.id],
        key_name=key_pair.key_name,
        tags={"Name": instance_name},
    )

    # Elastic IP
    eip = aws.ec2.Eip(
        "ec2-eip",
        domain="vpc",
    )

    aws.ec2.EipAssociation(
        "eip-association",
        instance_id=ec2.id,
        allocation_id=eip.id,
    )

    pulumi.export("public_ip", eip.public_ip)

    return ec2