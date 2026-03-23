# AWS Project: Secure S3 File Sharing with Event Notifications
## Overview

In this project, I designed and implemented a secure file-sharing solution using Amazon Web Services, enabling controlled access for an external user while maintaining visibility through automated notifications.

The solution simulates a real-world scenario where a media partner uploads product images, and administrators are notified of any changes.

## Architecture
- Amazon S3 Bucket – Central storage for shared images
- IAM User (External Partner) – Controlled access to specific folder
- Amazon SNS Topic – Event-driven notification system
- Email Subscription – Real-time alerts on changes
<br>
<img width="679" height="470" alt="image" src="https://github.com/user-attachments/assets/49fe5aca-6afe-4077-aaa9-5e810a91545d" />
<br>

## Key Implementations
### 1. Secure File Sharing with IAM
- Configured an external IAM user (mediacouser) with least privilege access
- Restricted access to:
  - Specific S3 bucket prefix (/images/)
- Allowed actions:
  - Upload (PutObject)
  - Read (GetObject)
  - Delete (DeleteObject)
- Prevented:
  - Bucket-level permission changes
  - Access outside the defined folder

### Implemented using IAM policies and groups in AWS Identity and Access Management

### 2. S3 Bucket Setup & Data Upload
- Created and configured an Amazon S3 bucket via AWS CLI

- Uploaded initial image dataset using:
  - aws s3 sync ~/initial-images/ s3://<bucket-name>/images
- Verified object storage and structure

📷 Add S3 bucket contents screenshot here

### 3. Event-Driven Notifications
- Created an Amazon Simple Notification Service topic
- Configured S3 to trigger events on:
- Object creation
- Object deletion
- Set up email subscription for real-time alerts

### Implemented bucket notification configuration using AWS CLI and JSON

### 4. Fine-Grained Event Filtering
- Notifications triggered only for /images/ prefix
- Avoided unnecessary alerts for other objects
### 5. End-to-End Testing
- Verified real-world use cases:
  - Upload → Email notification received
  - Delete → Email notification received
  - Unauthorized permission change → Access denied
  - Read operation → No notification (as expected)

📷 Add email notification screenshot here

## Technologies & Services Used
- Amazon S3 – Object storage
- Amazon SNS – Event notifications
- AWS Identity and Access Management – Access control
- Amazon EC2 – CLI host environment
- AWS CLI – Infrastructure and configuration
## Key Skills Demonstrated
- Designing secure cloud architectures (least privilege access)
- Implementing event-driven systems
- Managing IAM users, groups, and policies
- Automating infrastructure using AWS CLI
- Testing and validating real-world access scenarios
- Debugging permission and access issues
## Outcomes
- Built a secure and scalable file-sharing solution
- Enabled controlled external collaboration
- Implemented real-time monitoring via notifications
- Prevented unauthorized access through IAM policies
## What I Learned
- Importance of prefix-based access control in S3
- How event notifications integrate S3 with SNS
- Real-world application of least privilege principle
- Differences between allowed vs denied actions in IAM policies
📷 Screenshots
✅ IAM policy & permissions
✅ S3 bucket structure
✅ Upload/delete operations
✅ Email notifications (SNS)
✅ Access denied error (security validation)
## Possible Improvements
- Replace email notifications with:
- AWS Lambda for automated processing
- Add monitoring with Amazon CloudWatch
- Enable S3 versioning for recovery
- Use pre-signed URLs instead of IAM users for external sharing
