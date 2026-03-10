# config/config.py

"""
所有需要調整的設定集中在這裡
"""

# VPC
vpc_cidr = "10.0.0.0/16"

# Subnet
public_subnet_cidr = "10.0.1.0/24"

# EC2
instance_name = "pulumi-ec2"
instance_type = "t3.micro"

# SSH 白名單
ssh_allowed_cidr = "42.75.243.95/32"

# SSH Key
public_key_path = "/Users/james/.ssh/linha_id_rsa.pub"
keypair_name = "pulumi-basic-key"