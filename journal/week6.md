# Week 6 & 7 

These weeks werechallenging for me. Despite technical difficulties I faced while trying to fix the messaging system in production, I managed to accomplish a lot. I started by watching videos to improve my understanding of ECS security and Fargate technical questions. After that, I created ECR repos and pushed images for both the backend Flask app and frontend React JS app. I then deployed them as services to Fargate.

To manage my domain using Route53 via hosted zone, I provisioned and configured an Application Load Balancer along with target groups, created an SSL certificate via ACM, and set up record sets for the naked domain and API subdomain. Additionally, I configured CORS to only permit traffic from my domain.

To enhance the security of the Flask app, I made sure not to run it in debug mode and implemented a Refresh Token for Amazon Cognito. I also refactored the bin directory, configured task definitions to contain X-Ray, and turned on Container Insights. I created a Dockerfile for the production use case, and used Ruby to generate env dot files for Docker using ERB templates.

#### Fix messages in prod 
<img width="1735" alt="Screenshot 2023-04-05 at 18 01 42" src="https://user-images.githubusercontent.com/17580456/230988437-741ec591-9ca9-4d5c-b517-15a80cc66f90.png">

#### Configure task defintions to contain x-ray and turn on Container Insights	
<img width="1735" alt="Screenshot 2023-04-06 at 09 27 53" src="https://user-images.githubusercontent.com/17580456/230988443-76e37a3a-7e89-43ea-aa27-36608cd01488.png">

#### Buy domain via Route53 
<img width="1756" alt="Screenshot 2023-04-02 at 12 46 38" src="https://user-images.githubusercontent.com/17580456/230988946-eb490dae-4593-4b95-a85c-5e4853242f65.png">

#### Manage your domain useing Route53 via hosted zone	
<img width="1756" alt="Screenshot 2023-04-02 at 12 12 46" src="https://user-images.githubusercontent.com/17580456/230988937-bef53732-d2db-4a60-b02a-68a88437ea77.png">

#### Create an SSL cerificate via ACM	
<img width="1486" alt="Screenshot 2023-04-03 at 10 47 02" src="https://user-images.githubusercontent.com/17580456/230989289-6716abb2-b0d4-46e6-9b24-e57246ca65ae.png">








