# Week 1 — App Containerization

### VSCode Docker Extension
Docker for VSCode makes it easy to work with Docker

https://code.visualstudio.com/docs/containers/overview

Gitpod is preinstalled with theis extension -> in my case I did not see it, so I added it using the extensions tab. 

### Containerize Backend
Run in the terminal: 

    cd backend-flask
    export FRONTEND_URL="*"
    export BACKEND_URL="*"
    python3 -m flask run --host=0.0.0.0 --port=4567
    cd ..
    
* remember to install requirements.txt -> pip3 install -r requirements.txt   
* make sure to unlock the port on the port tab
* open the link for 4567 in your browser
* append to the url to /api/activities/home

I get back a json: 

<img width="1791" alt="image" src="https://user-images.githubusercontent.com/17580456/219962871-f31a4d28-75bf-44f6-a4ac-f401bc08e7ea.png">

### Add Dockerfile
Create a file here: backend-flask/Dockerfile

    FROM python:3.10-slim-buster

    WORKDIR /backend-flask

    COPY requirements.txt requirements.txt
    RUN pip3 install -r requirements.txt

    COPY . .

    ENV FLASK_ENV=development

    EXPOSE ${PORT}
    CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
    
### Build Container

    docker build -t  backend-flask ./backend-flask

This line creates a docker image from the dockerfile, but we still need to start the container (aka run it)

### Run Container

There are several options to pass the env variables, I used this: 

    docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask

Here I am running the backend application as a container in the background so that I can use my termal to print the running containers: 

<img width="1074" alt="image" src="https://user-images.githubusercontent.com/17580456/219962808-a5aa7d7f-17b9-45e4-9a86-159a7fd11eaa.png">

I see as images the basic slim-buster image that is used as a based as well as the one I created for my backend container: 

<img width="1074" alt="image" src="https://user-images.githubusercontent.com/17580456/219962842-fc75a983-22bd-48fe-908d-01d32f682b83.png">

I can also see data being returned as json if I go to the URL in ports (make sure is unlocked!) 

<img width="1791" alt="image" src="https://user-images.githubusercontent.com/17580456/219963324-aa56de42-80a6-48a8-b0d7-899b47cc7327.png">

### Send Curl to Test Server

To do the same in a de-attached way run: 

        docker container run --rm -p 4567:4567 -e FRONTEND_URL='*' -e BACKEND_URL='*' -d backend-flask
        
This allows us to use the terminal, so we can retrieve the JSON data this time using curl: 

        curl -X GET http://localhost:4567/api/activities/home -H "Accept: application/json" -H "Content-Type: application/json"

<img width="1409" alt="image" src="https://user-images.githubusercontent.com/17580456/219963902-6b200419-55e7-463f-befb-c0da5d3abfd3.png">

### Check Container Logs

    docker logs <CONTAINER_ID> -f
    
 Another way I try is: 
 
    docker logs $CONTAINER_ID -f

VSCODE makes it super easy to see the logs 

<img width="1277" alt="image" src="https://user-images.githubusercontent.com/17580456/219964446-f7d30fab-2522-4a8a-82bc-cf9d13d5e111.png">

### Gain Access to a Container

        docker exec -it <container_name or container_id> /bin/bash
        
<img width="762" alt="image" src="https://user-images.githubusercontent.com/17580456/219964761-d02e833e-49ed-4434-83ea-95120cb1372a.png">

### Delete an Image

        docker image rm backend-flask --force
        
 I can check by doing `docker images` that the image is gone. 
 
 ## Containerize Frontend
 
### Run NPM Install
We have to run NPM Install before building the container since it needs to copy the contents of node_modules

        cd frontend-react-js
        npm i

### Create Docker File
Create a file here: `frontend-react-js/Dockerfile`

### Build Container

        docker build -t frontend-react-js ./frontend-react-js

### Run Container

        docker run -p 3000:3000 -d frontend-react-js
        
Front-end is there but the data is missing because we need to add the back-end. 

<img width="1646" alt="image" src="https://user-images.githubusercontent.com/17580456/219965206-ba83310f-5f62-4664-8a14-f6fcc67977b0.png">

## Multiple Containers

### Create a docker-compose file

Create `docker-compose.yml` at the root of your project.This will allow us to RUN multiple containers. 

        version: "3.8"
        services:
          backend-flask:
            environment:
              FRONTEND_URL: "https://3000-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
              BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
            build: ./backend-flask
            ports:
              - "4567:4567"
            volumes:
              - ./backend-flask:/backend-flask
          frontend-react-js:
            environment:
              REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
            build: ./frontend-react-js
            ports:
              - "3000:3000"
            volumes:
              - ./frontend-react-js:/frontend-react-js

        # the name flag is a hack to change the default prepend folder
        # name when outputting the image names
        networks: 
          internal-network:
            driver: bridge
            name: cruddur
            
Docker compose up in VSCODE UI and we can see data!!   

<img width="1646" alt="image" src="https://user-images.githubusercontent.com/17580456/219967724-3a73c510-50bf-4708-ac83-6bbbfe142b9f.png">

## Adding DynamoDB Local and Postgres

We are going to use Postgres and DynamoDB local in future labs We can bring them in as containers and reference them externally

Lets integrate the following into our existing docker compose file:

### Postgres

        services:
          db:
            image: postgres:13-alpine
            restart: always
            environment:
              - POSTGRES_USER=postgres
              - POSTGRES_PASSWORD=password
            ports:
              - '5432:5432'
            volumes: 
              - db:/var/lib/postgresql/data
        volumes:
          db:
            driver: local
 
 To install the postgres client into Gitpod

          - name: postgres
            init: |
              curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
              echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
              sudo apt update
              sudo apt install -y postgresql-client-13 libpq-dev
  
 ## DynamoDB Local
 
         services:
          dynamodb-local:
            # https://stackoverflow.com/questions/67533058/persist-local-dynamodb-data-in-volumes-lack-permission-unable-to-open-databa
            # We needed to add user:root to get this working.
            user: root
            command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
            image: "amazon/dynamodb-local:latest"
            container_name: dynamodb-local
            ports:
              - "8000:8000"
            volumes:
              - "./docker/dynamodb:/home/dynamodblocal/data"
            working_dir: /home/dynamodblocal
            
 Example of using DynamoDB local https://github.com/100DaysOfCloud/challenge-dynamodb-local    

           
