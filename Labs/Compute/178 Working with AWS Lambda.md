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
<br><br>
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
✅ Decoupled architecture using multiple Lambda functionsv
✅ Email notifications via SNS<br>
✅ Dependency management using Lambda Layers<br>
Implementation Highlights
🔐 IAM & Security
Configured IAM roles with least-privilege access
Resolved permission issues (e.g., ssm:GetParameter, kms:Decrypt)
Managed secure access to database credentials
📦 Lambda Layers
Created a Lambda Layer for external dependency:
pymysql (for MySQL connectivity)
🗄️ Database Connectivity
Connected Lambda to MySQL database running on EC2
Fixed networking issue by opening port 3306 in the security group
📧 Notifications
Created SNS topic:
salesAnalysisReportTopic
Subscribed email endpoint for report delivery
⏱️ Scheduling
Configured cron trigger using EventBridge:
cron(0 20 ? * MON-SAT *)

⚠️ Note: AWS uses UTC time, which must be considered when scheduling jobs.

🧪 Troubleshooting & Debugging
Used CloudWatch Logs to diagnose:
IAM permission errors
Lambda timeout issues (resolved by increasing timeout)
Network connectivity problems
📸 Sample Output
📩 Automated email with daily sales report
📊 Data pulled dynamically from the database after new orders
📚 What I Learned
Designing event-driven serverless architectures
Managing IAM roles and permissions in real scenarios
Debugging distributed systems using CloudWatch
Handling secure configuration with Parameter Store
Working with Lambda layers and dependencies
Integrating multiple AWS services into a cohesive solution
💡 Future Improvements
Add CI/CD pipeline (e.g., GitHub Actions)
Replace EC2 database with Amazon RDS
Add error alerting (CloudWatch Alarms)
Store reports in S3 for historical tracking
Implement infrastructure as code (Terraform / CloudFormation)
🧠 Key Takeaway

This project demonstrates how to build a production-style automated reporting system using AWS serverless services, focusing on automation, security, and scalability.
