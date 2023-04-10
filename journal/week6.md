# Week 6 & 7 

This week was a challenging one for me. Despite technical difficulties I faced while trying to fix the messaging system in production, I managed to accomplish a lot. I started by watching videos to improve my understanding of ECS security and Fargate technical questions. After that, I created ECR repos and pushed images for both the backend Flask app and frontend React JS app. I then deployed them as services to Fargate.

To manage my domain using Route53 via hosted zone, I provisioned and configured an Application Load Balancer along with target groups, created an SSL certificate via ACM, and set up record sets for the naked domain and API subdomain. Additionally, I configured CORS to only permit traffic from my domain.

To enhance the security of the Flask app, I made sure not to run it in debug mode and implemented a Refresh Token for Amazon Cognito. I also refactored the bin directory, configured task definitions to contain X-Ray, and turned on Container Insights. I created a Dockerfile for the production use case, and used Ruby to generate env dot files for Docker using ERB templates.





