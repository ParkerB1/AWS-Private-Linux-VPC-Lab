# AWS Private Linux VPC Lab

## Project Overview
This project demonstrates a **secure cloud infrastructure setup** on AWS using a multi-tier architecture. The lab includes:

- A **VPC with public and private subnets**
- A **bastion host** (public EC2) to access a **private EC2 instance**
- A **Python web application** deployed on the private EC2
- **Monitoring and notifications** using CloudWatch and SNS
- **IAM roles, S3, CloudFront, and GitHub Actions** for CI/CD and deployments

The goal is to practice **real-world cloud networking, Linux server management, and AWS best practices** while building a portfolio-ready lab project.

---

## Architecture

**Key components:**

1. **VPC**  
   - 10.0.0.0/16 CIDR block  
   - 2 public subnets (different AZs) in 10.0.1.0/24 and 10.0.2.0/24 CIDR blocks
   - 2 private subnets (different AZs) in 10.0.11.0/24 and 10.0.12.0/24 CIDR blocks

2. **Public EC2 (Bastion Host)**  
   - Amazon Linux 2023  
   - Access point for SSH to private EC2  
   - Security group allows SSH from my all IPs due to github actions deployer IP being dynamic

3. **Private EC2 (App Server)**  
   - Amazon Linux 2023  
   - Runs a Python Flask web application behind a Gunicorn web server, all within a dedicated Python virtual environment (venv)
   - Only accessible via bastion host  
   - Uses IAM role for CloudWatch logs  

4. **Networking**  
   - Amazon Linux 2023 EC2 instance configured to be a NAT instance in public subnet for internet access from private subnet  
   - Security groups restrict traffic according to least-privilege principle  

5. **Monitoring & Notifications**  
   - CloudWatch monitors CPU and disk usage  
   - SNS sends email notifications for alarms  

6. **CI/CD Pipeline**  
   - GitHub Actions deploys application updates to EC2 via SSH  
   - Sample workflow triggers on code push  

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Cloud Provider | AWS (VPC, EC2, S3, CloudFront, IAM, SNS, CloudWatch) |
| OS | Amazon Linux 2023 |
| Programming | Python 3, Flask, Gunicorn, Nginx |
| CI/CD | GitHub Actions |
| Networking | Bastion host, NAT instance, public/private subnets |
| Monitoring | CloudWatch + SNS alerts |

---

## Setup Instructions

1. **Launch VPC & Subnets**  
   - Create public/private subnets  
   - Attach Internet Gateway to public subnets  
   - Set up NAT instance for private subnet outbound access  

2. **Launch EC2 Instances**  
   - Public EC2 as bastion host  
   - Private EC2 as app server  

3. **SSH Access**  
   - Use SSH agent forwarding from your laptop to connect to private EC2 via bastion host  
   - Configure key-based authentication for private EC2  

4. **Create Virtual Environment** on private EC2

```bash
sudo mkdir /opt/myFlaskApp
cd /opt/myFlaskApp
python3 -m venv venv
```

5. **Install Python & Dependencies** in the venv directory  

```bash
sudo dnf update -y
sudo dnf install python3 python3-pip -y
pip3 install flask gunicorn -y

```

6. **Deploy Flask App**
    - Sample app.py runs on private EC2
    - Systemd service manages Flask application
    - Nginx on public EC2 can acts as reverse proxy

7. **Monitoring**
    - Install CloudWatch agent on both EC2s
    - Configure alarms for CPU and disk usage
    - SNS notification trigger on alarm

8. **CI/CD**
    - GitHub Actions workflow deploys app code via SSH to EC2

9. **IaC Automation**
   - Designed a CloudFormation template that provisions the following:
   -- VPC with public and private subnets across multiple AZs
   -- Internet Gateway and routing for public subnets
   -- NAT instance for private subnet outbound access
   -- Bastion host (public EC2) with restricted SSH access
   -- Private EC2 application server
   -- Security groups following least-privilege principles
   -- IAM roles and instance profiles
   -- CloudWatch alarms and SNS notifications

---

## Project Highlights / Learning Outcomes
    - Designed a multi-tier AWS VPC with public/private subnets
    - Implemented bastion host for secure SSH access
    - Configured a private Linux EC2 instance with Python web app
    - Practiced Linux user management, SSH keys, and systemd services
    - Learned AWS monitoring & notifications (CloudWatch + SNS)
    - Built a lightweight CI/CD pipeline using GitHub Actions
    - Applied real-world security practices: least-privilege IAM, restricted SGs