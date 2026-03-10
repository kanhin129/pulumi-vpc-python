# Pulumi AWS VPC 範例專案 (Python)
使用 Pulumi + Python 3.9 在 AWS 上建立一個簡單的 VPC 基礎架構，透過 Infrastructure as Code (IaC) 的方式管理 AWS 資源。

開發環境為 macOS，並透過 Pulumi 自動部署 AWS Infrastructure。

---

## 專案目標

使用 Pulumi 設計並建立一個基本的 AWS VPC 環境，包含：

- VPC
- Public Subnet
- Internet Gateway
- Route Table
- Security Group
- EC2 Instance
- Elastic IP (EIP)

建立完成後 EC2 可以透過 SSH 遠端連線。

---

## Security Group 設定

| Port | 說明 | 來源 |
|-----|------|------|
| 22  | SSH | 指定白名單 IP |
| 80  | HTTP | 0.0.0.0/0 |
| 443 | HTTPS | 0.0.0.0/0 |

---

## 專案結構

pulumi-vpc-python/

__main__.py  
Pulumi.yaml  
requirements.txt  
README.md  

config/  
  config.py  

modules/  
  network.py  
  security_group.py  
  ec2.py  

---

## 檔案說明

config/config.py  
集中管理可調整設定，例如：

- VPC CIDR
- Subnet CIDR
- EC2 instance type
- SSH IP 白名單
- SSH public key 路徑

modules/network.py  
建立 VPC、Public Subnet、Internet Gateway 與 Route Table。

modules/security_group.py  
建立 Security Group 並設定 SSH、HTTP、HTTPS。

modules/ec2.py  
建立 EC2 Instance、AWS Key Pair 與 Elastic IP。

__main__.py  
Pulumi 程式入口，負責呼叫各模組建立 AWS Infrastructure。

---

## 開發環境

- macOS
- Python 3.9
- Pulumi CLI
- AWS CLI

---

## 安裝與設定

安裝 Pulumi

brew install pulumi

設定 AWS 認證

aws configure

輸入：

AWS Access Key  
AWS Secret Access Key  
Region  

安裝 Python 套件

pip install -r requirements.txt

---

## 部署 Infrastructure

初始化 Pulumi stack

pulumi stack init dev

部署 AWS infrastructure

pulumi up

部署完成後會顯示 EC2 Public IP。

---

## SSH 連線 EC2

ssh -i ~/.ssh/linha_id_rsa ec2-user@EC2_PUBLIC_IP

---

## 刪除 Infrastructure

pulumi destroy

---

## 總結

本專案示範如何使用 Pulumi 與 Python 建立 AWS VPC 基礎架構，並透過模組化方式管理 Network、Security 與 Compute，使 Infrastructure 可以透過程式碼進行版本控制、部署與管理。