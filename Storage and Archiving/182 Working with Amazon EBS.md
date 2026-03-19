# Managing Storage on AWS (EBS & S3)

## Project Overview
This lab demonstrates how to manage cloud storage using AWS services, focusing on Amazon EBS snapshots and Amazon S3 versioning.

The project showcases automation, data lifecycle management, and version control to ensure efficient and reliable storage operations.

## Objectives
- Automate backup creation using EBS snapshots  
- Implement retention logic to manage storage costs  
- Manage file versioning and synchronization with Amazon S3  
- Use AWS CLI and Python scripts for operational efficiency
  
## Technologies Used
- AWS CLI  
- Amazon EC2 / EBS  
- Amazon S3  
- Python (automation scripts)  

## Part 1: EBS Snapshot Management
### Instance Configuration
An instance profile was attached to the processor EC2 instance to enable permissions for snapshot operations.
<img width="452" height="126" alt="image" src="https://github.com/user-attachments/assets/1b77d906-6460-4315-a540-07fa5a9ffb55" />

An IAM role was attached to the instance
<img width="452" height="138" alt="image" src="https://github.com/user-attachments/assets/f641a332-418c-490c-9dcf-7204935b1205" />

---

### Initial Snapshot Creation
Steps performed via AWS CLI:
- Retrieved the instance ID  
- Stopped the instance  
- Created an initial snapshot of the EBS volume  
- Verified snapshot completion  
- Restarted the instance  

---

### 🔹 Snapshot Automation
A scheduled process was configured to automate snapshot creation at regular intervals.

As a result:
- Multiple snapshots were generated over time  
- Backup consistency was ensured without manual intervention  

---

### 🔹 Retention Policy Implementation
A Python script was implemented to retain only the **two most recent snapshots**, deleting older ones.

Example command used to list snapshots:

```bash
aws ec2 describe-snapshots --filters "Name=volume-id, Values=vol-0eeedd71a657372c9" --query 'Snapshots[*].SnapshotId'
```

- Before cleanup: 5 snapshots  
- After script execution: Only 2 snapshots retained  

This demonstrates efficient storage lifecycle management and cost optimization.

---

## ⚙️ Part 2: File Management with S3

### 🔹 File Download & Setup
Files were downloaded and prepared on the EC2 instance:

```bash
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/.../files.zip
unzip files.zip
```

---

### 🔹 S3 Versioning Activation
Before syncing files, versioning was enabled on the S3 bucket to track changes and prevent accidental data loss.

---

### 🔹 File Synchronization
The local directory was synchronized with the S3 bucket:
- Files were uploaded and verified  
- A file was deleted locally and in S3  
- Deletion behavior was validated  

---

### 🔹 Version Control Validation
- File versions were inspected using version IDs  
- The local folder was re-synced  
- A new version of `file1.txt` was successfully created in S3  

This confirmed proper version tracking and recovery capability.

---

## 💡 Key Skills Demonstrated
- Cloud storage management (EBS & S3)  
- Automation using AWS CLI and Python  
- Backup and retention strategy implementation  
- Version control and data integrity management  
- Troubleshooting and validation of cloud operations  

---

## 📈 Business Value
This project demonstrates the ability to:
- Implement automated backup solutions  
- Optimize storage costs through retention policies  
- Ensure data reliability and recoverability  
- Apply structured, scalable cloud storage practices  

---

## 🚀 Future Improvements
- Automate workflows using AWS Lambda  
- Add monitoring with CloudWatch  
- Implement lifecycle policies for S3 storage classes  
