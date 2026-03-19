## Validation & Pre-Deployment Testing

Before deploying the website to Amazon S3, a local testing environment was established to validate functionality, layout, and user experience.

### Environment Setup
A lightweight local server was configured using Python to simulate a live environment, enabling early-stage validation of website behavior.

<img width="1812" height="876" alt="image" src="https://github.com/user-attachments/assets/616a61b1-9d89-4580-a7b2-2ff13f7473c1" />

Development and file management were carried out using Visual Studio Code, supporting efficient iteration and version control.
<img width="1812" height="732" alt="image" src="https://github.com/user-attachments/assets/49c3f862-6b47-453c-80d6-729403bf004d" />

### Functional Validation
All web pages were tested locally via a localhost server to ensure:
- Correct rendering of layouts  
- Proper navigation between pages  
- Consistency of visual elements  
<img width="2790" height="1714" alt="image" src="https://github.com/user-attachments/assets/1be7498c-7912-4d44-a388-3694c5471db8" />

### Issue Identification & Resolution
Following deployment to S3, a discrepancy was identified where certain visual assets (images) were not displayed correctly.
<img width="1934" height="950" alt="image" src="https://github.com/user-attachments/assets/9e36e2b8-2053-4e3e-a6d7-83480e27c29c" />

A root cause analysis determined that the issue was due to missing files in the deployment package. The gap was resolved by uploading the required assets to the S3 bucket.
<img width="1934" height="950" alt="image" src="https://github.com/user-attachments/assets/e1a9dd0d-abbc-4ad1-8b9a-40726b1928e9" />

The final result
<img width="1934" height="950" alt="image" src="https://github.com/user-attachments/assets/ac9bcd34-df64-4b45-ad23-e64b64478b38" />

### Key Takeaways
- Applied validation techniques prior to deployment to reduce production issues  
- Identified and resolved data/asset gaps impacting user experience  
- Demonstrated structured problem-solving and root cause analysis  
- Ensured alignment between expected and actual system behavior  

