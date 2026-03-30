# Migrating a Web Application Database from Local MariaDB to AWS RDS (Secure SSL Connection)

## Overview

In this project, I migrated a PHP-based café web application from a local MariaDB database (running on EC2) to a managed Amazon RDS MariaDB instance.

## Architecture
- EC2 Instance → Hosts PHP web application
- Amazon RDS (MariaDB) → Managed database
- AWS Systems Manager Parameter Store → Stores configuration
- SSL (global-bundle.pem) → Secure DB connection
🛠️ Technologies Used
AWS EC2
AWS RDS (MariaDB)
PHP
MySQL / MariaDB CLI
Linux (Amazon Linux)
SCP (file transfer)
SSL/TLS
🔄 Migration Steps
1. Verify Local Database
Connected to local MariaDB on EC2
Identified tables:
order
order_item
product
product_group

📸 [Add screenshot: SHOW TABLES]

2. Create Database Backup
mysqldump -u root -p'Re:Start!9' cafe_db > cafedb-backup.sql

📸 [Add screenshot of dump file]

3. Create Amazon RDS Instance
Launched MariaDB RDS instance
Enabled require_secure_transport

📸 [Add RDS configuration screenshot]

4. Import Data into RDS
mysql -u root -p \
--host=<RDS-ENDPOINT> \
--ssl-ca=global-bundle.pem \
cafe_db < cafedb-backup.sql

📸 [Add successful import screenshot]

5. Troubleshooting Connection Issues

Encountered and resolved:

❌ ssl-mode=VERIFY_CA not supported
❌ insecure transport error
❌ access denied
❌ unknown database
❌ host formatting issues

✅ Solution:

Used --ssl-ca
Corrected command syntax
Verified credentials
6. Update Application Configuration
Modified Parameter Store to point to RDS endpoint
Identified that PHP app did not support SSL by default
7. Debug PHP Application

Issues encountered:

SSL connection failure
Reserved keyword (order)
Schema mismatch:
id vs order_number
order_date vs order_date_time
8. Create Custom PHP Files

Created:

menu_rds.php → reads products from RDS
orders_rds.php → reads orders from RDS

Key fixes:

Added SSL connection via PDO
Corrected SQL queries
Used backticks for reserved table names

📸 [Add browser output screenshots]

🔐 Key Learning: SSL Enforcement

RDS required secure connections:

require_secure_transport = ON

Fix:

--ssl-ca=global-bundle.pem
🧠 Key Learnings
Difference between local DB vs managed cloud DB
Importance of SSL in production environments
Debugging real-world errors:
Connection issues
Schema mismatches
SQL syntax problems
Understanding application–database integration
🧩 Challenges Faced
Issue	Resolution
Cannot connect to RDS	Added SSL
Unknown columns	Matched schema
Reserved table name	Used backticks
PHP not connecting	Created custom connection
SCP issues	Fixed permissions & paths
✅ Final Result
Application successfully reads data from Amazon RDS
Secure SSL connection established
Orders and menu displayed correctly

📸 [Final working app screenshot]
