import pulumi
import pulumi_aws as aws

def create_ec2(subnet, security_group, key_name, instance_name="basic-ec2"):
    # 取得最新 Amazon Linux 2 AMI
    ami = aws.ec2.get_ami(
        most_recent=True,
        owners=["amazon"],
        filters=[{"name": "name", "values": ["amzn2-ami-hvm-*-x86_64-gp2"]}]
    )

    # 建立 EC2
    ec2_instance = aws.ec2.Instance(
        instance_name,
        instance_type="t3.micro",
        ami=ami.id,
        subnet_id=subnet.id,
        vpc_security_group_ids=[security_group.id],
        key_name=key_name,
        associate_public_ip_address=True,
        tags={"Name": instance_name},
    )

    # 建立 Elastic IP，直接綁定 EC2
    eip = aws.ec2.Eip(
        f"{instance_name}-eip",
        instance=ec2_instance.id  # 不需要 vpc=True
    )

    # Export Elastic IP
    pulumi.export(f"{instance_name}_public_ip", eip.public_ip)

    return ec2_instance
