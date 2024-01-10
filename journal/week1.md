# Week 1 — App Containerization

**INSTALLING DOCKER EXTENSION**  
i. Click on the **Extension** icon on the dashboard on the left   
ii. Search **Docker** and ensure you select the verified option from Microsoft (with a blue tick)  
iii. Install  

## 1. Containerize Backend 

### Install Flask
We need to install Flask since we'll use it in creating our web app  
```
cd backend-flask
pip3 install -r requirements.txt
```

### Create the Docker file
Create a docker file named **Dockerfile** in the **backend-flask dir**  

```docker
FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=4567"]
```

### Build the Container Image
Run  
``docker build -t backend-flask ./backend-flask``  

### Run the Container
Run the command  
``docker run --rm -d -p 4567:4567 -it -e FRONTEND_URL="*" -e BACKEND_URL="*"  backend-flask``  

## Containerize Frontend

### Install NPM
We have to run NPM install before building the container as it requires node_modules  
```
cd ../frontend-react-js
npm i
```
### Create Docker file in **frondend-react-js dir**  
```
