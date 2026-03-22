# Serverless Sales Analysis Report with AWS Lambda
## Project Overview

This project demonstrates a serverless data pipeline on AWS that generates and emails a daily sales report.

The solution uses AWS Lambda, EventBridge (CloudWatch Events), SNS, Systems Manager Parameter Store, and EC2 (LAMP stack) to automate data extraction, analysis, and reporting.

<img width="452" height="230" alt="image" src="https://github.com/user-attachments/assets/f601ac79-1e11-4037-b0ee-1e5c2167ed7b" />
<br>
The system runs automatically every day and sends a sales summary via email.

## Architecture

### Workflow:

A scheduled event (Amazon EventBridge) triggers the main Lambda function daily.
<br>
The main function (salesAnalysisReport) invokes a secondary Lambda (salesAnalysisReportDataExtractor).
<br>
The data extractor queries a MySQL database hosted on EC2.
<br>
Results are returned to the main function.
<br>
The report is formatted and sent to an SNS topic.
<br>
SNS delivers the report via email.
<br>
### AWS Services Used
<br>
AWS Lambda – Serverless compute for report generation
<br>
Amazon EventBridge (CloudWatch Events) – Scheduled trigger (cron job)
<br>
Amazon SNS – Email notifications
<br>
AWS Systems Manager Parameter Store – Secure storage of DB credentials
<br>
Amazon EC2 (LAMP stack) – MySQL database backend
<br>
IAM – Roles and permissions management
<br>
CloudWatch Logs – Monitoring and debugging
<br>

### Key Features 
✅ Fully serverless reporting workflow <br>
✅ Secure database credential management via Parameter Store<br>
✅ Automated daily execution using cron scheduling<br>
✅ Decoupled architecture using multiple Lambda functions<br>
✅ Email notifications via SNS<br>
✅ Dependency management using Lambda Layers<br>

### Implementation Highlights
### IAM & Security
Configured IAM roles with least-privilege access
<img width="452" height="211" alt="image" src="https://github.com/user-attachments/assets/cfc3b7ec-2672-4c2a-98ca-ef97d45ffb6c" />
<br>
Resolved permission issues<br>
<img width="452" height="206" alt="image" src="https://github.com/user-attachments/assets/8e0ad8ed-bf94-4805-962e-bd7de8ff1fc4" />
<br>
Managed secure access to database credentials
<br>
### Lambda Layers
<br>
Created a Lambda Layer for external dependency:
<br>
<img width="452" height="139" alt="image" src="https://github.com/user-attachments/assets/620fe810-ed0e-45f7-af2f-5058e8f65d34" />
<br>
Created a data extractor Lambda function
<br>
<img width="452" height="223" alt="image" src="https://github.com/user-attachments/assets/d74a9e1a-8cda-42ef-b106-76bd49882ee7" />
<br>
Added the lambda layer to the function
<br>
<img width="452" height="284" alt="image" src="https://github.com/user-attachments/assets/c94d5fbc-d630-4c4e-a75c-936dc3f9c598" />
<br>
Imported the code for the data extractor Lambda function
<img width="452" height="284" alt="image" src="https://github.com/user-attachments/assets/80e8cafc-572b-4bfa-b0fe-247e196151a8" />
<br>
<img width="452" height="213" alt="image" src="https://github.com/user-attachments/assets/26a7f517-c1d6-446d-a038-33792a036f8c" /><br>

### Connectivity
Configured network settings for the function
<img width="452" height="233" alt="image" src="https://github.com/user-attachments/assets/3b778874-2b06-4468-9d36-66e4a16ddd5d" /><br>

### Testing
Tested the data extractor Lambda function
<br>
<img width="452" height="233" alt="image" src="https://github.com/user-attachments/assets/e3a34861-dde6-47dc-b373-15b8c710f9e2" /><br>
<img width="452" height="241" alt="image" src="https://github.com/user-attachments/assets/625f9c0a-aed8-4ae0-9db1-6156da032aee" /><br>
there was an error<br>
<img width="452" height="181" alt="image" src="https://github.com/user-attachments/assets/ae02a1ee-defc-45e2-859d-b718a1c7a950" />
<br>
Fixed networking issue by opening port 3306 in the security group.<br>
<img width="452" height="234" alt="image" src="https://github.com/user-attachments/assets/c3f5539a-f76f-407c-b0f5-70a1440fb3aa" /><br>
<img width="452" height="121" alt="image" src="https://github.com/user-attachments/assets/947c7e88-7005-44ad-8756-b8faec12c9f7" /><br>
after the changes in the security group, the error is now gone<br>
<img width="452" height="82" alt="image" src="https://github.com/user-attachments/assets/962f1c62-79a1-4c01-8227-378176abd818" /><br>
### Placing an order and testing again
<img width="452" height="191" alt="image" src="https://github.com/user-attachments/assets/168f89ef-026b-4827-8a29-80e0d86621ba" /><br>
<img width="452" height="191" alt="image" src="https://github.com/user-attachments/assets/fd5d07a1-8d35-4774-854a-b98880785887" /><br>

### Notifications
Created SNS topic<br>
<img width="452" height="171" alt="image" src="https://github.com/user-attachments/assets/d5bf3705-bf45-4e92-b928-6ddd0aeffa35" /><br>
Subscribed email endpoint for report delivery<br>
<img width="452" height="149" alt="image" src="https://github.com/user-attachments/assets/6f9b07db-a862-4851-b52c-12b70d769d9a" /><br>
<img width="452" height="221" alt="image" src="https://github.com/user-attachments/assets/9f5dccf7-f99b-4d9e-871a-5f2d6107b02a" /><br>

### Sales Analysis Report
Connecting to the CLI host instance<br>
<img width="452" height="136" alt="image" src="https://github.com/user-attachments/assets/7cea2032-dad3-4724-ade0-135b8bf66d49" /><br>
Configuring AWS CLI
<img width="452" height="148" alt="image" src="https://github.com/user-attachments/assets/f71f1572-439e-456d-b9c2-3631136aca9c" /><br>
Creating the SalesAnalysisReport Lambda function<br>
<img width="452" height="163" alt="image" src="https://github.com/user-attachments/assets/cabcfb6b-ba95-4f2c-9082-908aa8540588" /><br>
<img width="452" height="163" alt="image" src="https://github.com/user-attachments/assets/e54bd0d2-61a8-457e-9830-c468936b8985" /><br>
function was working<br>
<img width="452" height="163" alt="image" src="https://github.com/user-attachments/assets/bc84effc-c71e-47d6-8fd7-a4fdabf99782" /><br>
received the email notification<br>
<img width="452" height="422" alt="image" src="https://github.com/user-attachments/assets/db3654e2-ef44-42bf-acbb-a7b5ce155aba" />

### Scheduling
Configured cron trigger using EventBridge:<br>
cron(0 20 ? * MON-SAT *)<br>
<img width="452" height="203" alt="image" src="https://github.com/user-attachments/assets/0481d91a-4e6e-4ee3-a6e9-7d3537f5a511" /><br>


⚠️ Note: AWS uses UTC time, which must be considered when scheduling jobs.

### What I Learned
Designing event-driven serverless architectures<br>
Managing IAM roles and permissions in real scenarios<br>
Debugging distributed systems using CloudWatch<br>
Handling secure configuration with Parameter Store<br>
Working with Lambda layers and dependencies<br>
Integrating multiple AWS services into a cohesive solution<br>

### Key Takeaway

This project demonstrates how to build a production-style automated reporting system using AWS serverless services, focusing on automation, security, and scalability.
