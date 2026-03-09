# Pulumi Basic AWS VPC

這是一個簡單的 Pulumi Python 專案，用於建立最基本的 AWS VPC 架構，面試範例可用。

## 架構

- VPC (10.0.0.0/16)
- 1 Public Subnet
- Internet Gateway
- Public Route Table
- Security Group (SSH & HTTP)

## 使用方式

1. Clone 專案
```bash
git clone <你的-git-repo-url>
cd pulumi-basic-vpc

2. 建立虛擬環境（可選）
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. 設定 AWS 認證
aws configure

4. 部署
pulumi stack init dev
pulumi up

5. 刪除資源
pulumi destroy
