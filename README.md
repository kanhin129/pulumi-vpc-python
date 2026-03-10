# Pulumi AWS VPC 範例專案 (Python)

本專案使用 **Pulumi + Python 3.9** 在 **AWS** 上建立一個簡單且完整的 VPC 基礎架構，並將程式碼以 Infrastructure as Code (IaC) 的方式管理。

開發環境為 **macOS**，並透過 Pulumi 部署 AWS 資源。

---

## 專案目標

使用 Pulumi 設計並建立一個基本且完整的 AWS VPC 環境，包含網路、路由、安全群組與 EC2，並可透過 SSH 遠端連線。

---

## 建立的 AWS 資源

本專案會建立以下 AWS 基礎架構：

- VPC
- Public Subnet
- Internet Gateway
- Route Table
- Route Table Association
- Security Group
- EC2 Instance
- Elastic IP (EIP)
- AWS Key Pair

---
Internet
│
▼
Internet Gateway
│
▼
VPC (10.0.0.0/16)
│
▼
Public Subnet (10.0.1.0/24)
│
├── EC2 Instance
└── Elastic IP
---

## 安全群組設定

Security Group 設定如下：

| Port | 說明 | 來源 |
|-----|------|------|
| 22  | SSH 遠端登入 | 指定白名單 IP |
| 80  | HTTP | 0.0.0.0/0 |
| 443 | HTTPS | 0.0.0.0/0 |

---

## 專案結構
pulumi-vpc-python/
├── main.py
├── Pulumi.yaml
├── requirements.txt
├── README.md
├── config
│ └── config.py
└── modules
├── network.py
├── security_group.py
└── ec2.py


各檔案說明：

- `config/config.py`  
  集中管理可調整的設定，例如 VPC CIDR、EC2 類型、SSH IP 白名單等。

- `modules/network.py`  
  建立 VPC、Public Subnet、Internet Gateway 與 Route Table。

- `modules/security_group.py`  
  建立 Security Group 並設定 SSH / HTTP / HTTPS 規則。

- `modules/ec2.py`  
  建立 EC2、Key Pair 與 Elastic IP。

- `__main__.py`  
  Pulumi 程式入口，負責呼叫各模組建立資源。

---

## 開發環境

本專案使用以下環境：

- macOS
- Python 3.9
- Pulumi
- AWS CLI

---

## 安裝 Pulumi

macOS 可以使用 Homebrew 安裝：

```bash
brew install pulumi
```

使用 AWS CLI 設定帳號：
aws configure
AWS Access Key
AWS Secret Key
Region

安裝 Python 套件
pip install -r requirements.txt

初始化 Pulumi Stack
pulumi stack init dev

部署 AWS Infrastructure
pulumi up

SSH 連線 EC2
ssh -i ~/.ssh/linha_id_rsa ec2-user@<EC2_PUBLIC_IP>

刪除 Infrastructure
pulumi destroy

1.使用 pulumi 設計一個 "完整"  aws vpc(請包含您對於軟體架構的理解進行規劃)，將程式碼推送到任一個 public git repo，並在 README 簡扼說明該專案的內容。(請包涵整個 pulumi 環境配置、設定) ps: 請提供連結
2.嘗試設計一個 gitlab 常見的 cicd pipeline 以 yaml 形式為主