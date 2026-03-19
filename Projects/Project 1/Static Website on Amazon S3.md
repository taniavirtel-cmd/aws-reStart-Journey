<b>Configuring a static website on Amazon S3</b>

Amazon S3 is an excellent choice for hosting static websites because it provides a highly scalable, durable, and cost-effective storage solution with minimal configuration.

The website was created in a sandbox environment. </br>
<img width="452" height="151" alt="image" src="https://github.com/user-attachments/assets/f9843622-6df6-47bf-9f98-f7e4a7442f74" />

First step was to create a bucket.
<img width="786" height="392" alt="image" src="https://github.com/user-attachments/assets/a1e28211-de0e-4cb5-8513-dd64ab17432a" />

Then edit some important parameters such as:
Enable static web hosting
Define the index page (main page of the website)
Define the error page
<img width="2116" height="836" alt="image" src="https://github.com/user-attachments/assets/8bb3f7ff-af22-4413-911a-070f163495fe" />

Very quickly we had the website endpoint
<img width="2116" height="484" alt="image" src="https://github.com/user-attachments/assets/68dd2b11-ccca-4ba3-90f5-bfbf5a0f1e33" />

but if we try to access it, there's an error. There's still work to do!
<img width="2116" height="484" alt="image" src="https://github.com/user-attachments/assets/943440d1-e2f3-4edf-b4dc-65cb9d75fe3c" />

There was a block on public access.This setting needs to be changed
<img width="2116" height="328" alt="image" src="https://github.com/user-attachments/assets/9205f257-edb2-4978-b24c-161b5590585c" />

<img width="2116" height="638" alt="image" src="https://github.com/user-attachments/assets/ee036590-a343-4a65-9d83-0bbf978b9062" />

A bucket policy is also needed (a set of rules that controls who can access your data in an Amazon S3 bucket and what actions they’re allowed to perform)
<img width="1478" height="970" alt="image" src="https://github.com/user-attachments/assets/13f847c7-3545-4bb3-a474-880d093fadb6" />

Now we upload the files that make our website (HTML + images)
<img width="2144" height="696" alt="image" src="https://github.com/user-attachments/assets/fe07748c-7263-4bf9-9735-1215bf10bfbd" />

Images are very important, we worked hard on the look of our website
<img width="1075" height="473" alt="Screenshot 2026-03-19 at 13 58 02" src="https://github.com/user-attachments/assets/9f1832a7-ab7d-424f-8eaa-9a4ef62ec840" />

Once everything was uploaded, the Quiet Kettle was finally live
<img width="1075" height="473" alt="Screenshot 2026-03-19 at 13 58 02" src="https://github.com/user-attachments/assets/9f1832a7-ab7d-424f-8eaa-9a4ef62ec840" />

