# __main__.py

from modules.network import create_network
from modules.security_group import create_security_group
from modules.ec2 import create_ec2

# 建立網路
vpc, public_subnet = create_network()

# Security Group
sg = create_security_group(vpc)

# EC2
ec2 = create_ec2(public_subnet, sg)