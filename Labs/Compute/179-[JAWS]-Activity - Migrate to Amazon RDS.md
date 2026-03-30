# Migrating a Web Application Database from Local MariaDB to AWS RDS (Secure SSL Connection)

## Overview

In this project, I migrated a PHP-based café web application from a local MariaDB database (running on EC2) to a managed Amazon RDS MariaDB instance.

## Architecture
- EC2 Instance → Hosts PHP web application
- Amazon RDS (MariaDB) → Managed database
- AWS Systems Manager Parameter Store → Stores configuration
- SSL (global-bundle.pem) → Secure DB connection
## Technologies Used
- AWS EC2
- AWS RDS (MariaDB)
- PHP
- MySQL / MariaDB CLI
- Linux (Amazon Linux)
- SCP (file transfer)
- SSL/TLS
## Migration Steps
1. Verify Local Database
Connected to local MariaDB on EC2
Identified tables:
order
order_item
product
product_group
<br>
<img width="452" height="145" alt="image" src="https://github.com/user-attachments/assets/88980aa2-cddc-46b1-a68c-2d9f92cc5555" />
<br>
<img width="452" height="64" alt="image" src="https://github.com/user-attachments/assets/56ee8271-ef28-430d-86c3-8ec4a6607f75" />
<br>
2. Create Database Backup
mysqldump -u root -p'Re:Start!9' cafe_db > cafedb-backup.sql
<br>
<img width="452" height="145" alt="image" src="https://github.com/user-attachments/assets/b5a76c0b-deba-4cce-abc5-2e21057a26d5" />
<br>
<img width="452" height="13" alt="image" src="https://github.com/user-attachments/assets/58090283-e7f9-46ed-a9c9-d307c5a39032" />
<br>
<img width="452" height="194" alt="image" src="https://github.com/user-attachments/assets/9f48218c-6c15-4c30-8804-f1a90519e757" />
<br>

3. Create Amazon RDS Instance
Launched MariaDB RDS instance
Enabled require_secure_transport
<br>
<img width="452" height="219" alt="image" src="https://github.com/user-attachments/assets/0da55d57-2e09-4241-84c6-c02955453f63" />
<br>
<img width="452" height="86" alt="image" src="https://github.com/user-attachments/assets/9abb6d69-3dde-4be0-842e-7feac21863d3" />
<br>

4. Import Data into RDS
mysql -u root -p \
--host=<RDS-ENDPOINT> \
--ssl-ca=global-bundle.pem \
cafe_db < cafedb-backup.sql
<br>
<img width="452" height="193" alt="image" src="https://github.com/user-attachments/assets/e1b3afe8-93ae-4c1b-ac87-ca2cd020c776" />
<br>
changed the parameter /cafe/dbUrl to the new database<br>
<img width="452" height="193" alt="image" src="https://github.com/user-attachments/assets/9be15c33-0156-4a6c-b159-9c1799e79276" />
<br>

6. Troubleshooting Connection Issues

Encountered and resolved:

❌ ssl-mode=VERIFY_CA not supported - the original php tried normal connection, had to replace it for one using SSL
<br>
<img width="452" height="118" alt="image" src="https://github.com/user-attachments/assets/14d282e8-9b0d-4a84-95c3-0025f642c6fe" />

<img width="452" height="283" alt="image" src="https://github.com/user-attachments/assets/aac45bb7-a756-4a66-b6eb-97d364b2df28" />

<br>
❌ insecure transport error
<br>
❌ access denied<br>
❌ unknown database<br>
❌ host formatting issues<br>

✅ Solution:

Used --ssl-ca<br>
<img width="590" height="441" alt="image" src="https://github.com/user-attachments/assets/3bb1096c-98da-4e9f-ac93-f2c1839e39d2" />
<br>
Corrected command syntax<br>
Verified credentials<br>
6. Update Application Configuration<br>
Modified Parameter Store to point to RDS endpoint<br>
Identified that PHP app did not support SSL by default<br>
7. Debug PHP Application

Issues encountered:

SSL connection failure
Reserved keyword (order)
Schema mismatch:
id vs order_number
order_date vs order_date_time
8. Create Custom PHP Files

Created:

menu_rds.php → reads products from RDS<br>
orders_rds.php → reads orders from RDS<br>
<img width="693" height="196" alt="image" src="https://github.com/user-attachments/assets/0e8deca6-b54e-464d-9aa7-57775426ee2e" />
<br>
<img width="692" height="498" alt="image" src="https://github.com/user-attachments/assets/f31b8a11-4038-4cf1-94c0-cd006a5233fe" />
<br>
Key fixes:

Added SSL connection via PDO
Corrected SQL queries
Used backticks for reserved table names (such as Order)

🔐 Key Learning: SSL Enforcement

RDS required secure connections:

require_secure_transport = ON

Fix:

--ssl-ca=global-bundle.pem
## Key Learnings
- Difference between local DB vs managed cloud DB
- Importance of SSL in production environments
- Debugging real-world errors:
- Connection issues
- Schema mismatches
- SQL syntax problems
- Understanding application–database integration
## Challenges Faced
- Issue	Resolution
- Cannot connect to RDS	Added SSL
- Unknown columns	Matched schema
- Reserved table name	Used backticks
- PHP not connecting	Created custom connection
- SCP issues	Fixed permissions & paths
## Final Result
- Application successfully reads data from Amazon RDS
- Secure SSL connection established
- Orders and menu displayed correctly
