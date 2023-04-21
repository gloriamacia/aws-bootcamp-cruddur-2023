# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

This week, I had a great time learning about AWS code build and code pipeline services with the Cruddur backend. I want to give a big shoutout to "jamesoundb" and "anle4s" - two awesome bootcampers who helped me out with some issues I was having, one with the log groups and the other with the missing permissions in a video. Proof of my work can be seen in the journal. 

However, I have to say that since week 5 of the bootcamp, it's been a real challenge keeping up with the workload, even when just completing the checklist items. It's been taking me around 10-12 hours per week, and it's been tough to maintain that level of commitment even though I really enjoy the material.

So, I was thrilled to finally have a bit of a break with week 9 (CI/CD), which required less than four hours of video. It's also been really fun getting to know some of the other bootcampers - the crew (as can be seen on Discord) really got much smaller in the last 2-3 weeks. Thanks again for organizing this. 

Getting the build to work on aws code build... 
<img width="1335" alt="Screenshot 2023-04-20 at 00 01 43" src="https://user-images.githubusercontent.com/17580456/233727983-1ec22f36-c77a-4213-bbcf-a9ecf9b88771.png">

This policy statement was missing (thanks anle4s!) 

      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
              "ecr:BatchCheckLayerAvailability",
              "ecr:CompleteLayerUpload",
              "ecr:GetAuthorizationToken",
              "ecr:InitiateLayerUpload",
              "ecr:PutImage",
              "ecr:UploadLayerPart",
              "ecr:BatchGetImage",
              "ecr:GetDownloadUrlForLayer"
            ],
            "Resource": "*"
          }
        ]
      }
      

Very important to check this box!! otherwise the build will fail:

<img width="1335" alt="Screenshot 2023-04-20 at 00 03 06" src="https://user-images.githubusercontent.com/17580456/233728003-afeed16e-250d-464a-af7b-a603bbb0577f.png">

Proof of entire pipeline running green - on code pipeline: 

<img width="462" alt="Screenshot 2023-04-20 at 23 04 41" src="https://user-images.githubusercontent.com/17580456/233728012-65181f71-2676-48d1-affc-2cdee8309e17.png">

Proof of new health-check working in the backend after code pipeline running: 

<img width="434" alt="Screenshot 2023-04-20 at 23 19 57" src="https://user-images.githubusercontent.com/17580456/233728013-0acdb542-df87-4997-b648-f990fc34fb78.png">
