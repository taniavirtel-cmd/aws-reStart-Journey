Deploying a Static Website on Amazon S3 (Lab 170b)

## Project Overview ##

This lab demonstrates how to deploy a static website to Amazon S3 using AWS CLI and IAM for access management. It highlights cloud deployment, automation, and best practices for secure S3 operations.

## Objectives

After completing this lab, you should be able to:

Run AWS CLI commands using IAM and Amazon S3 services

Deploy a static website to an S3 bucket

Create a script to copy files from a local directory to Amazon S3

Understand basic S3 bucket configuration and permissions

### Tasks & Implementation
Task 1: Connect to an Amazon Linux EC2 instance using SSM

Accessed the EC2 instance using AWS Systems Manager (SSM). Amazon Linux comes pre-installed with the AWS CLI.

Task 2: Configure the AWS CLI

Updated AWS CLI credentials for the session

Task 3: Create an S3 Bucket

Created a new S3 bucket using the AWS CLI:

<img width="452" height="47" alt="image" src="https://github.com/user-attachments/assets/81e628df-d372-42ce-932b-b85887959e9c" />

Task 4: Create an IAM User with Full S3 Access

Created a dedicated IAM user and attached the AmazonS3FullAccess policy:
<img width="452" height="76" alt="image" src="https://github.com/user-attachments/assets/b44be997-b64f-49b5-9cd5-371ce8895226" />

This ensures secure, managed access to S3 resources.

Task 5: Adjust S3 Bucket Permissions

Configured bucket permissions to allow public access for website content while maintaining security best practices.
<img width="452" height="96" alt="image" src="https://github.com/user-attachments/assets/c54372c5-f2ee-4bf1-83d0-80ba4846a568" />
<img width="452" height="317" alt="image" src="https://github.com/user-attachments/assets/cb2faea1-a3d1-4020-abfa-424df4a1be76" />

<img width="452" height="172" alt="image" src="https://github.com/user-attachments/assets/63273494-4196-489c-91f7-d76e2f8c45a8" />

Task 6: Extract Lab Files

Downloaded and prepared website files for deployment on the EC2 instance.
<img width="452" height="28" alt="image" src="https://github.com/user-attachments/assets/dceba212-a9d2-410f-a3fa-30ec4d988454" />

Task 7: Upload Files to Amazon S3

Deployed the static website to S3 and configured it as a website endpoint:
<img width="452" height="87" alt="image" src="https://github.com/user-attachments/assets/3114e9c7-a2c9-4d79-9b2b-ea37fd648b9f" />
<img width="452" height="268" alt="image" src="https://github.com/user-attachments/assets/bb1ac93f-384c-4ff0-872e-aa815f0fe044" />

Task 8: Automate Website Updates

Created a batch script to make future website updates repeatable:

## Key Skills Demonstrated

Static website deployment on AWS S3

IAM user creation and policy management

AWS CLI proficiency and automation

Secure bucket configuration and public access management

Repeatable deployment workflows using scripts

## Business Value

Demonstrates ability to deploy scalable, cost-effective cloud solutions

Ensures secure access management and automation in cloud operations

Builds practical experience for cloud-based web hosting projects
