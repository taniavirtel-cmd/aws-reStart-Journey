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
  <img width="452" height="218" alt="image" src="https://github.com/user-attachments/assets/c1cf84b2-a74d-42df-856c-188bced7b248" />

- Restricted access to:
  - Specific S3 bucket prefix (/images/)<br>
    <img width="452" height="218" alt="image" src="https://github.com/user-attachments/assets/4ea4d923-f012-4cf8-aca5-0c43e6080171" />

- Allowed actions:
  - Upload (PutObject)<br>
    <img width="452" height="220" alt="image" src="https://github.com/user-attachments/assets/4a4e9ae4-7cbe-4f9d-a6c9-ccf5a7ae954b" />

  - Read (GetObject)
  - Delete  (DeleteObject)
    <br><img width="272" height="72" alt="image" src="https://github.com/user-attachments/assets/83514f9d-66a8-4438-9fd0-1f3b63f8b34f" />

    
- Prevented:
  - Bucket-level permission changes<br>
  <img width="452" height="183" alt="image" src="https://github.com/user-attachments/assets/b36e18cf-7a08-49a8-b210-7a570e0577cc" /><br>

  - Access outside the defined folder

### Implemented using IAM policies and groups in AWS Identity and Access Management

### 2. S3 Bucket Setup & Data Upload
- Created and configured an Amazon S3 bucket via AWS CLI<br>
<img width="452" height="35" alt="image" src="https://github.com/user-attachments/assets/834599b5-a3e2-4ff0-9cd9-dc132b7355f9" /><br>

- Uploaded initial image dataset using:
  - aws s3 sync ~/initial-images/ s3://<bucket-name>/images<br>
  <img width="452" height="66" alt="image" src="https://github.com/user-attachments/assets/9acb2377-332e-407d-a98c-120fc2c47179" /><br>

- Verified object storage and structure<br>
<img width="452" height="79" alt="image" src="https://github.com/user-attachments/assets/36542675-66f6-4ace-8c26-f9b4ddb83250" /><br>


### 3. Event-Driven Notifications
- Created an Amazon Simple Notification Service topic<br>
  <img width="452" height="151" alt="image" src="https://github.com/user-attachments/assets/ae34b684-62ab-4577-9270-59030d927b32" /><br>

- Configured S3 to trigger events on:
- Object creation
- Object deletion
- Set up email subscription for real-time alerts<br>
<img width="452" height="28" alt="image" src="https://github.com/user-attachments/assets/f1dc019d-79f9-44e7-be07-007f35528115" /><br>
<img width="452" height="224" alt="image" src="https://github.com/user-attachments/assets/fa251d66-7d4f-40c6-b19a-7760a275966c" />


### Implemented bucket notification configuration using AWS CLI and JSON

### 4. Fine-Grained Event Filtering
- Notifications triggered only for /images/ prefix
- Avoided unnecessary alerts for other objects
### 5. End-to-End Testing
- Verified real-world use cases:
  - Upload → Email notification received<br>
  <img width="452" height="318" alt="image" src="https://github.com/user-attachments/assets/07d52d55-e90c-4fde-a23f-79dabb591859" /><br>

  - Delete → Email notification received<br>
  <img width="452" height="310" alt="image" src="https://github.com/user-attachments/assets/4f3467cf-b0c7-459b-88f9-4bac6e1ebe24" /><br>

  - Unauthorized permission change → Access denied<br>
    <img width="452" height="33" alt="image" src="https://github.com/user-attachments/assets/f4510c2b-5b95-45a3-a704-3fd6da83eff3" /><br>

  - Read operation → No notification (as expected)<br>
<img width="452" height="68" alt="image" src="https://github.com/user-attachments/assets/35e8c489-9eb7-4d99-9a6e-b1eb173007fd" /><br>

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

