# Pulumi Basic AWS VPC

這是一個簡單的 Pulumi Python 專案，用於建立最基本的 AWS VPC 架構，面試範例可用。

## 架構

pulumi-basic-vpc/
├── __main__.py       # 主要呼叫
├── vpc.py            # VPC + Subnet + IGW + RouteTable
├── security.py       # Security Group
├── ec2.py            # EC2 建立
├── Pulumi.yaml       # Pulumi 專案設定
├── requirements.txt  # Python 套件
└── README.md


## 使用方式

1. Clone 專案
```bash
git clone 
cd pulumi-basic-vpc

2. 建立虛擬環境（可選）
#python3 -m venv .venv
#source .venv/bin/activate

pip install -r requirements.txt

3. 設定 AWS 認證
aws configure
Access Key
Secret Key
region: ap-east-2

4. 部署
pulumi stack init dev
pulumi up

5. 刪除資源
pulumi destroy
