# Static Website Hosting on Amazon S3

Amazon S3 is an excellent choice for hosting static websites because it provides a highly scalable, durable, and cost-effective storage solution with minimal configuration.

## Project Summary
This project demonstrates how to configure and deploy a static website using Amazon S3. It highlights key cloud concepts such as storage configuration, access control, and web hosting without server management.

## Tools & Technologies
- Amazon S3  
- HTML / CSS  
- AWS Management Console  

## Implementation Steps
The website was created in a sandbox environment. </br>
<img width="452" height="151" alt="image" src="https://github.com/user-attachments/assets/f9843622-6df6-47bf-9f98-f7e4a7442f74" />

### 1. Create an S3 Bucket
- Created a new S3 bucket to store website files.
<img width="786" height="392" alt="image" src="https://github.com/user-attachments/assets/a1e28211-de0e-4cb5-8513-dd64ab17432a" />

### 2. Enable Static Website Hosting
- Enabled static website hosting
- Defined index and error documents
<img width="2116" height="836" alt="image" src="https://github.com/user-attachments/assets/8bb3f7ff-af22-4413-911a-070f163495fe" />

### 3. Retrieve Website Endpoint
- Generated the S3 website endpoint
- Initial access returned an error due to permissions
<img width="2116" height="484" alt="image" src="https://github.com/user-attachments/assets/68dd2b11-ccca-4ba3-90f5-bfbf5a0f1e33" />

The error
<img width="2116" height="484" alt="image" src="https://github.com/user-attachments/assets/943440d1-e2f3-4edf-b4dc-65cb9d75fe3c" />

### 4. Configure Public Access
- Disabled "Block Public Access"
- Allowed public access to bucket content
<img width="2116" height="328" alt="image" src="https://github.com/user-attachments/assets/9205f257-edb2-4978-b24c-161b5590585c" />

<img width="2116" height="638" alt="image" src="https://github.com/user-attachments/assets/ee036590-a343-4a65-9d83-0bbf978b9062" />

### 5. Apply Bucket Policy
- Added a bucket policy to allow public read access
- Ensured secure and controlled exposure of files
<img width="1478" height="970" alt="image" src="https://github.com/user-attachments/assets/13f847c7-3545-4bb3-a474-880d093fadb6" />

### 6. Upload Website Files
- Uploaded HTML and image assets
<img width="2144" height="696" alt="image" src="https://github.com/user-attachments/assets/fe07748c-7263-4bf9-9735-1215bf10bfbd" />

Images are very important, we worked hard on the look of our website
<img width="1075" height="473" alt="Screenshot 2026-03-19 at 13 58 02" src="https://github.com/user-attachments/assets/9f1832a7-ab7d-424f-8eaa-9a4ef62ec840" />

## Final Output
The website “Quiet Kettle” was successfully deployed and accessible via the S3 endpoint.
<img width="2712" height="1446" alt="image" src="https://github.com/user-attachments/assets/b0e56d35-22fb-4650-9c2b-e5eb367d682b" />
<br><br>
<img width="2712" height="1446" alt="image" src="https://github.com/user-attachments/assets/96821ac3-8e21-4895-b89e-ed3b2bc6c10b" />
<br><br>
<img width="2712" height="1446" alt="image" src="https://github.com/user-attachments/assets/7b5ce91c-77be-4e00-bee8-5c27781d5267" />
<br><br>
<img width="2712" height="1446" alt="image" src="https://github.com/user-attachments/assets/ca8e6f64-187b-4373-84d8-8b776a3c270a" />
<br><br>
<img width="2712" height="1514" alt="image" src="https://github.com/user-attachments/assets/2ce48955-ea53-4362-b093-5217e2677a12" />

## Key Skills Demonstrated
- Cloud storage configuration (AWS S3)
- Access control and security (bucket policies, public access settings)
- Static website deployment
- Troubleshooting access and permission issues

## Business Value
This project demonstrates the ability to:
- Deliver cost-efficient web hosting solutions
- Configure secure and scalable cloud infrastructure
- Translate technical setup into practical business applications

## Next Improvements
- Integrate Amazon CloudFront for CDN performance
- Add custom domain with Route 53
- Implement HTTPS using SSL certificates
