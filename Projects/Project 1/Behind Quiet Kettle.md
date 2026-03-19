Validation & Pre-Deployment Testing

Before deploying the website to Amazon S3, a local testing environment was established to validate functionality, layout, and user experience.

Environment Setup

A lightweight local server was configured using Python to simulate a live environment, enabling early-stage validation of website behavior.

<img width="1812" height="876" alt="image" src="https://github.com/user-attachments/assets/616a61b1-9d89-4580-a7b2-2ff13f7473c1" />

An editor was also required such as Visual Studio Code
<img width="1812" height="732" alt="image" src="https://github.com/user-attachments/assets/49c3f862-6b47-453c-80d6-729403bf004d" />

From here html pages could be tested before a final upload to S3, as you can see below everything was first on a localhost
<img width="2790" height="1714" alt="image" src="https://github.com/user-attachments/assets/1be7498c-7912-4d44-a388-3694c5471db8" />

Still once in the bucket we had issues like missing images
<img width="1934" height="950" alt="image" src="https://github.com/user-attachments/assets/9e36e2b8-2053-4e3e-a6d7-83480e27c29c" />

One quick upload to the bucket, and the page was fixed
<img width="1934" height="950" alt="image" src="https://github.com/user-attachments/assets/e1a9dd0d-abbc-4ad1-8b9a-40726b1928e9" />

<img width="1934" height="950" alt="image" src="https://github.com/user-attachments/assets/ac9bcd34-df64-4b45-ad23-e64b64478b38" />


