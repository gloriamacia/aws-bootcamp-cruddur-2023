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



