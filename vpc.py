import pulumi_aws as aws

# 建立 VPC
vpc = aws.ec2.Vpc(
    "basic-vpc",
    cidr_block="10.0.0.0/16",
    enable_dns_support=True,
    enable_dns_hostnames=True,
    tags={"Name": "basic-vpc"},
)

# 取得可用 AZ
azs = aws.get_availability_zones(state="available").names

# 建立 public subnet
public_subnet = aws.ec2.Subnet(
    "public-subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    availability_zone=azs[0],
    tags={"Name": "public-subnet"},
)

# Internet Gateway
igw = aws.ec2.InternetGateway(
    "basic-igw",
    vpc_id=vpc.id,
    tags={"Name": "basic-igw"},
)

# Public Route Table
public_rt = aws.ec2.RouteTable(
    "public-rt",
    vpc_id=vpc.id,
    tags={"Name": "public-rt"},
)

# Route 指向 IGW
aws.ec2.Route(
    "public-route",
    route_table_id=public_rt.id,
    destination_cidr_block="0.0.0.0/0",
    gateway_id=igw.id
)

# Route Table Association
aws.ec2.RouteTableAssociation(
    "public-rta",
    subnet_id=public_subnet.id,
    route_table_id=public_rt.id
)
