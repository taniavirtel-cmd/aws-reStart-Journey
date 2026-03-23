# AWS Project: Public File Hosting with Amazon S3
## Overview

In this project, I implemented a basic object storage and public access solution using Amazon Web Services.

The goal was to:

- Store files in the cloud
- Control access permissions
- Make specific content publicly accessible via a browser

## Architecture
- CLI Host (EC2) – Used for AWS CLI operations
- Amazon S3 Bucket – Stores uploaded objects
- Public Object Access – Enabled via object-level permissions

### Key Implementations
### 1. AWS CLI Configuration
- Connected to EC2 instance using EC2 Instance Connect
- Configured AWS CLI with credentials:
  - aws configure<br>
 <img width="452" height="177" alt="image" src="https://github.com/user-attachments/assets/40e05fbd-3ff9-4381-a6fb-7191ac50eb39" />
<br>
### 2. S3 Bucket Creation

- Created a uniquely named Amazon S3 bucket using CLI:<br>
<img width="452" height="34" alt="image" src="https://github.com/user-attachments/assets/48db9a19-b19e-4a38-b0a8-0ee240be6405" />
<br>
aws s3 mb s3://<bucket-name> --region us-west-2
### 3. Object Upload

- Uploaded a file from my computer to the EC2 instance:<br>
  <img width="452" height="145" alt="image" src="https://github.com/user-attachments/assets/c8708c71-1064-452c-815d-b4efb97d67ee" />
<br>
- Uploaded the file from the EC2 instance to the S3 bucket<br>
<img width="452" height="30" alt="image" src="https://github.com/user-attachments/assets/594c74f5-0358-450c-bebf-f29e4fc87f14" />

aws s3 cp file.jpg s3://<bucket-name>/

### 4. Access Control (Object-Level Security)
Initially, object was not publicly accessible<br>
<img width="452" height="120" alt="image" src="https://github.com/user-attachments/assets/5f13fb5c-8349-45b1-ba48-4623bc0740e0" />
<br>
Updated permissions to allow public read access. I could not change the block public access setting, as I don't want the whole bucket to be accessible.<br>
<img width="452" height="107" alt="image" src="https://github.com/user-attachments/assets/4e60d8ae-2717-4af1-9f79-435e8b862e67" />
<br>
I created a 3 hour URL with public access to my specific object
<img width="452" height="16" alt="image" src="https://github.com/user-attachments/assets/9e548ad8-7f7f-4757-8626-79fb02b31dd1" />
<br>
I could also have changed the bucket policy indicating my specific object, but I did not have rights with my lab user.<br>
### Important:

Only the object was made public
The bucket remained private (best practice)
### 5. Browser Access

Accessed the object via URL:

<br>
<img width="452" height="202" alt="image" src="https://github.com/user-attachments/assets/329133f0-899f-4c11-86f8-57241c29ec53" />
<br>

### 6. Listing Bucket Contents

Verified uploaded objects using:
<img width="452" height="25" alt="image" src="https://github.com/user-attachments/assets/74e690cd-4c98-43d4-b94d-db381c3b20a7" />

## Technologies & Services Used
- Amazon S3 – Object storage
- Amazon EC2 – CLI host
- AWS CLI – Resource management
## Key Skills Demonstrated
- Creating and managing cloud storage
- Using AWS CLI for automation
- Understanding S3 access control (private vs public)
- Applying object-level permissions
- Testing and validating access via browser
## Outcomes
- Successfully uploaded and hosted a file in S3
- Controlled access using object-level permissions
- Enabled secure public access without exposing the entire bucket
## What I Learned
- Difference between:
  - Bucket-level vs object-level permissions
- Default S3 security (everything is private)
- How public access works via object URLs
- Importance of limiting public exposure
