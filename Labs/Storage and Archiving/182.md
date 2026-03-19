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
  
<img width="452" height="149" alt="image" src="https://github.com/user-attachments/assets/fdea38f3-bb6b-451b-ad04-d22385cb6754" />

<img width="452" height="122" alt="image" src="https://github.com/user-attachments/assets/cc8ad472-be68-4db8-a189-c354cefc4d40" />

<img width="452" height="150" alt="image" src="https://github.com/user-attachments/assets/f683e109-7973-4478-8a9c-fd903931d182" />

---

### Snapshot Automation
A scheduled process was configured to automate snapshot creation at regular intervals.

As a result:
- Multiple snapshots were generated over time  
- Backup consistency was ensured without manual intervention
  
<img width="452" height="178" alt="image" src="https://github.com/user-attachments/assets/62f3f9ff-3dad-417a-b657-dda9258daa0a" />

<img width="452" height="240" alt="image" src="https://github.com/user-attachments/assets/2d3dd6ac-454e-423b-9231-310cb35f5296" />

---

### Retention Policy Implementation
A Python script was implemented to retain only the **two most recent snapshots**, deleting older ones.

<img width="452" height="266" alt="image" src="https://github.com/user-attachments/assets/45465386-54f3-4974-aeaf-0a6c80723044" />


Example command used to list snapshots:

```bash
aws ec2 describe-snapshots --filters "Name=volume-id, Values=vol-0eeedd71a657372c9" --query 'Snapshots[*].SnapshotId'
```

- Before cleanup: 5 snapshots  
- After script execution: Only 2 snapshots retained  

<img width="452" height="61" alt="image" src="https://github.com/user-attachments/assets/285fa31f-1ada-419a-a35c-72125bb6fcb6" />

<img width="452" height="70" alt="image" src="https://github.com/user-attachments/assets/ef925ad2-293a-4e0b-8def-7e621a9ee7c5" />


This demonstrates efficient storage lifecycle management and cost optimization.

---

## Part 2: File Management with S3

### File Download & Setup
Files were downloaded and prepared on the EC2 instance:

```bash
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/.../files.zip
unzip files.zip
```
<img width="452" height="213" alt="image" src="https://github.com/user-attachments/assets/09aee10e-8a7c-4655-8e9f-9b785f728f33" />

---

### Versioning Activation
Before syncing files, versioning was enabled on the S3 bucket to track changes and prevent accidental data loss.

<img width="452" height="26" alt="image" src="https://github.com/user-attachments/assets/73ca889e-a12d-468c-92e3-55f92ffc4248" />


---

### File Synchronization
The local directory was synchronized with the S3 bucket:
- Files were uploaded and verified  
- A file was deleted locally and in S3  
- Deletion behavior was validated  

<img width="452" height="85" alt="image" src="https://github.com/user-attachments/assets/45a1843e-3d60-4c90-814b-171b4d43c05f" />

in S3
<img width="452" height="46" alt="image" src="https://github.com/user-attachments/assets/5717e521-95fa-496a-bfb8-1a7b49a2d718" />

<img width="452" height="54" alt="image" src="https://github.com/user-attachments/assets/9f939d7d-5118-46d7-bcdc-9958e89a3a50" />

---

### Version Control Validation
- File versions were inspected using version IDs  
- The local folder was re-synced  
- A new version of `file1.txt` was successfully created in S3  

<img width="452" height="232" alt="image" src="https://github.com/user-attachments/assets/dc3d833e-9bf6-4068-87e7-1401f58915cc" />

<img width="452" height="95" alt="image" src="https://github.com/user-attachments/assets/a657e079-8d0c-4304-bcde-a1cc8a50aa3d" />

<img width="452" height="42" alt="image" src="https://github.com/user-attachments/assets/4f9b45db-e625-4ff8-b9b1-cb4469340e84" />


This confirmed proper version tracking and recovery capability.

---

## Key Skills Demonstrated
- Cloud storage management (EBS & S3)  
- Automation using AWS CLI and Python  
- Backup and retention strategy implementation  
- Version control and data integrity management  
- Troubleshooting and validation of cloud operations  

---

## Business Value
This project demonstrates the ability to:
- Implement automated backup solutions  
- Optimize storage costs through retention policies  
- Ensure data reliability and recoverability  
- Apply structured, scalable cloud storage practices  

---

## Future Improvements
- Automate workflows using AWS Lambda  
- Add monitoring with CloudWatch  
- Implement lifecycle policies for S3 storage classes  
