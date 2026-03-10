# modules/security_group.py

import pulumi_aws as aws
from config.config import ssh_allowed_cidr


def create_security_group(vpc):

    sg = aws.ec2.SecurityGroup(
        "ec2-sg",
        vpc_id=vpc.id,
        description="Allow SSH, HTTP and HTTPS access",
        ingress=[
            {
                "protocol": "tcp",
                "from_port": 22,
                "to_port": 22,
                "cidr_blocks": [ssh_allowed_cidr],
                "description": "Allow SSH from my IP",
            },
            {
                "protocol": "tcp",
                "from_port": 80,
                "to_port": 80,
                "cidr_blocks": ["0.0.0.0/0"],
                "description": "Allow HTTP from anywhere",
            },
            {
                "protocol": "tcp",
                "from_port": 443,
                "to_port": 443,
                "cidr_blocks": ["0.0.0.0/0"],
                "description": "Allow HTTPS from anywhere",
            },
        ],
        egress=[
            {
                "protocol": "-1",
                "from_port": 0,
                "to_port": 0,
                "cidr_blocks": ["0.0.0.0/0"],
                "description": "Allow all outbound traffic",
            }
        ],
        tags={"Name": "ec2-sg"},
    )

    return sg