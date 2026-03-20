## AWS Project – Managing Storage & Data Lifecycle Automation
### Overview

Designed and implemented a storage management solution on AWS using Amazon EC2, Amazon EBS, and Amazon S3. The project focused on automating snapshot lifecycle management and ensuring data durability through version-controlled object storage.

### Key Responsibilities & Achievements
1. EBS Snapshot Management & Automation

Attached an IAM instance profile to an EC2 processor instance to enable secure AWS CLI operations.

Created and managed Amazon EBS snapshots via AWS CLI to back up volume data.

Automated snapshot creation using scheduled Python scripts.

Implemented a retention policy to optimize storage costs by keeping only the latest 2 snapshots.

Example CLI command used:
