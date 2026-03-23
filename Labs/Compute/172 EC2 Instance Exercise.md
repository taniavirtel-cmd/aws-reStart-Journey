# AWS Project: Deploying a Web Application on EC2

## Overview

In this project, I created a web application on an Amazon EC2 instance within a custom virtual network on Amazon Web Services.

The project demonstrates core cloud engineering skills including network configuration, instance provisioning, and web server deployment.

## Architecture
- Custom VPC with subnet
- Internet Gateway for external access
- Route Table for public routing
- EC2 Instance (Amazon Linux) hosting a web server
- Security Group allowing SSH and HTTP access

## Key Implementation Steps
### 1. Network Setup<br>
Created a custom VPC and subnet<br><br>
Configured:
  - Internet Gateway
  - Route table for public access
  - Enabled auto-assign public IP
### 2. EC2 Instance Deployment
Launched an instance using:
  - Amazon Linux AMI
  - t2.micro instance type
  - General Purpose SSD (gp2) storage<br><br>
  <img width="452" height="203" alt="image" src="https://github.com/user-attachments/assets/7fd76167-37b2-419d-810c-0a6ac522ee5f" />

Configured security groups:<br>
  - SSH (port 22)
  - HTTP (port 80)
### 3. Web Server Configuration
Installed and started Apache (httpd) using user data script<br>
Configured permissions for /var/www/html<br>
Verified installation through system logs<br>
### 4. Application Deployment
Connected via EC2 Instance Connect (SSH)<br>
Deployed a custom HTML page:<br>
  - Stored in /var/www/html<br>
  - Successfully accessed the application via public IP<br>

📷 Add screenshot of system logs here
📷 Add screenshot of working web page here

## Technologies & Services Used
- Amazon EC2 – Compute
- Amazon VPC – Networking
- Apache HTTP Server – Web hosting
- EC2 Instance Connect – Secure access
- Linux (Amazon Linux) – OS

## Key Skills Demonstrated
- Cloud infrastructure setup (VPC, routing, networking)
- Secure instance configuration (SSH, security groups)
- Web server deployment and configuration
- Troubleshooting connectivity and deployment issues
- Understanding of public vs private networking in AWS
## Outcome
- Successfully deployed a publicly accessible web application
- Built a complete cloud-based architecture from scratch
- Demonstrated ability to configure, secure, and validate AWS resources
## What I Learned
- Importance of correct network routing and internet gateway setup
- How security groups control access to cloud resources
- Using user data scripts for automation
- End-to-end deployment workflow from infrastructure to application

## Screenshots
✅ EC2 system log (httpd installation)
✅ Running web application in browser
🚀 Next Steps (Optional Improvements)
Add a load balancer for scalability
Use Amazon CloudFront for performance
Automate deployment using Infrastructure as Code (e.g., CloudFormation)
