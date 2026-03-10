# modules/network.py

import pulumi_aws as aws
from config.config import vpc_cidr, public_subnet_cidr


def create_network():

    # VPC
    vpc = aws.ec2.Vpc(
        "main-vpc",
        cidr_block=vpc_cidr,
        enable_dns_support=True,
        enable_dns_hostnames=True,
        tags={"Name": "main-vpc"},
    )

    # AZ
    azs = aws.get_availability_zones(state="available")

    # Public Subnet
    public_subnet = aws.ec2.Subnet(
        "public-subnet",
        vpc_id=vpc.id,
        cidr_block=public_subnet_cidr,
        availability_zone=azs.names[0],
        map_public_ip_on_launch=True,
        tags={"Name": "public-subnet"},
    )

    # Internet Gateway
    igw = aws.ec2.InternetGateway(
        "main-igw",
        vpc_id=vpc.id,
        tags={"Name": "main-igw"},
    )

    # Route Table
    public_rt = aws.ec2.RouteTable(
        "public-rt",
        vpc_id=vpc.id,
        routes=[
            {
                "cidr_block": "0.0.0.0/0",
                "gateway_id": igw.id,
            }
        ],
        tags={"Name": "public-rt"},
    )

    # Route Table Association
    aws.ec2.RouteTableAssociation(
        "public-rta",
        subnet_id=public_subnet.id,
        route_table_id=public_rt.id,
    )

    return vpc, public_subnet