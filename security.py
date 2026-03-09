import pulumi_aws as aws
from vpc import vpc

sg = aws.ec2.SecurityGroup(
    "basic-sg",
    vpc_id=vpc.id,
    description="Allow SSH and HTTP",
    ingress=[
        {"protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["42.75.243.95/32"]},
        {"protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"]},
    ],
    egress=[
        {"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]}
    ],
    tags={"Name": "basic-sg"},
)
