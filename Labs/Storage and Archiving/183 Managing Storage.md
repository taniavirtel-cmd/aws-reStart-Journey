# AWS Project: EBS Snapshot Automation & S3 Data Synchronization
## Overview

In this project, I implemented an automated storage management solution on Amazon Web Services, focusing on data durability, lifecycle management, and backup recovery.

The project demonstrates how to:
- Automate EBS snapshot creation and retention
- Synchronize data between compute storage and object storage
- Recover deleted data using versioning

## Architecture
- EC2 (Command Host) – Administration via AWS CLI
- EC2 (Processor) – Attached EBS volume for data storage
- Amazon EBS – Block storage for instance data
- Amazon S3 – Object storage for backup and sync
- IAM Role (Instance Profile) – Secure service access
<br>
<img width="452" height="282" alt="image" src="https://github.com/user-attachments/assets/21c90da6-b11e-4673-a48e-6a4a04d57fbc" />
<br>

## Key Implementations
### 1. Storage & Access Setup
- Created an S3 bucket for data synchronization
- Attached IAM role (instance profile) to EC2 for secure access to:
  - Amazon S3
  - Amazon EBS<br>
    <img width="452" height="126" alt="image" src="https://github.com/user-attachments/assets/204c71b9-ceff-418c-891e-c777cc085e9f" />
    <br>
    <img width="452" height="138" alt="image" src="https://github.com/user-attachments/assets/d5fa8653-12bb-46a8-9f7c-eaa952502e54" /><br>

  
### 2. EBS Snapshot Automation
- Identified and managed EBS volumes via AWS CLI<br>
  <img width="452" height="149" alt="image" src="https://github.com/user-attachments/assets/77b2c238-07f5-42bf-a1a0-0b7295a2762d" /><br>

- Created initial snapshot after safely stopping the instance<br>
    <img width="452" height="122" alt="image" src="https://github.com/user-attachments/assets/47e36712-0547-4c91-916f-57a3b61f22a8" /><br>
                                                        
- Automated snapshot creation using cron jobs<br>
<img width="452" height="178" alt="image" src="https://github.com/user-attachments/assets/2ea55b0b-d5e4-42be-9ac6-91b235eeb781" /><br>

- Implemented lifecycle control using a Python script to:
  - Retain only the latest 2 snapshots<br>
    <img width="452" height="240" alt="image" src="https://github.com/user-attachments/assets/74b67e7b-a8e8-4af5-89c0-6bf8648ca59b" /><br>
    <img width="452" height="266" alt="image" src="https://github.com/user-attachments/assets/ac007c8c-3dc1-4e72-98e6-93dd770095b6" /><br>

  - Automatically delete older snapshots<br>
    <img width="452" height="70" alt="image" src="https://github.com/user-attachments/assets/82819bd1-edc9-438d-bd1d-2c074fb38f75" /><br>



### 3. Data Synchronization with S3

Synced local files to S3 using:

- aws s3 sync files s3://<bucket-name>/files/<br>
  <img width="452" height="213" alt="image" src="https://github.com/user-attachments/assets/440fb1ce-0222-4f3f-b199-1b1793b5e0e3" /><br>

- Enabled S3 versioning for data protection<br>
  <img width="452" height="26" alt="image" src="https://github.com/user-attachments/assets/190b3482-2ad2-40e8-a784-aa95cb9a27a6" />

- Used --delete flag to maintain sync consistency between local and S3<br>
  <img width="452" height="85" alt="image" src="https://github.com/user-attachments/assets/746320dc-6d06-4b4f-84b0-9410b52dac74" /><br>
  <img width="452" height="46" alt="image" src="https://github.com/user-attachments/assets/a6903309-9bba-4b8d-85a2-513a4f3719ba" /><br>

### 4. Data Recovery & Versioning
- Retrieved deleted files using S3 versioning:
- Listed object versions<br>
  <img width="452" height="232" alt="image" src="https://github.com/user-attachments/assets/bc6f5251-0101-41df-ab09-9c85a16707da" /><br>

- Restored previous versions using AWS CLI<br>
  <img width="452" height="42" alt="image" src="https://github.com/user-attachments/assets/982aae79-c2d1-4f12-a98e-c890440a0d57" /><br>

- Demonstrated data recovery without data loss


## Technologies & Services Used
- Amazon EC2 – Compute
- Amazon EBS – Persistent storage
- Amazon S3 – Object storage & backup
- AWS CLI – Automation & scripting
- Python – Snapshot lifecycle management
- Linux (cron) – Task scheduling

## Key Skills Demonstrated
- Storage lifecycle management and backup strategies
- Automation using AWS CLI and scripting
- Secure access using IAM roles and instance profiles
- Data synchronization between storage services
- Disaster recovery using versioning
- Troubleshooting and validation of cloud resources

## Outcomes
- Automated EBS snapshot creation and retention
- Reduced storage overhead by cleaning up old snapshots
- Ensured data durability with S3 backup and versioning
- Successfully restored deleted files using version control

## What I Learned
- Importance of automated backups and retention policies
- Differences between block storage (EBS) and object storage (S3)
- How versioning enables recovery without traditional backups
- Using CLI + scripting for repeatable cloud operations

## Possible Improvements
- Automate the workflow using:
  - AWS Lambda
  - Amazon EventBridge
- Implement monitoring with Amazon CloudWatch
- Add lifecycle policies directly in S3 for cost optimization
