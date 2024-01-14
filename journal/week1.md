# Week 1 — App Containerization

## Required Homework

### 1. Containerize Backend 
#### Install Flask
We need to install Flask since we'll use it in creating our web app  
```
cd backend-flask
pip3 install -r requirements.txt
```

#### Create the Docker file
Create a docker file named **Dockerfile** in the **backend-flask dir**  

```dockerfile
FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=4567"]
```

#### Build the Container Image
Run  
``docker build -t backend-flask ./backend-flask``  

#### Run the Container
Run the command  
``docker run --rm -d -p 4567:4567 -it -e FRONTEND_URL="*" -e BACKEND_URL="*"  backend-flask`` 

> **--rm** deletes the container immediately it is stopped
> **-d** runs the container in a *detached* mode
> Unlock the ports on the **PORT Tab** after the container has been created  
> Click on the port URL and append to the url **/api/activities/home**. The result will be a json

### 2. Containerize Frontend
#### Install NPM
We have to run NPM install before building the container as it'll copy contents of the node_modules folder  
```
cd ../frontend-react-js
npm i
```

#### Create Docker file in **frontend-react-js dir**  
```dockerfile
FROM node:16.18

ENV PORT=3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD [ "npm", "start"]
```

#### Build the Container Image
Run  
``docker build -t frontend-react-js ./frontend-react-js``

#### Run the Container
Run the command  
``docker run --rm -d -p 3000:3000 -it frontend-react-js``  

> Unlock the ports on the **PORT Tab** after the container has been created and click on the URL

### 3. Multiple Container Orchestration
#### Create Docker compose file
To automate the creation of the images and containers for the front and backend, write the following code in a **docker-compose.yml** file  
```yml
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
  front-react-js:
    environment:
      REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./frontend-react-js
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/frontend-react-js

networks:
  internal-network:
    driver: bridge
    name: cruddur
```

#### Verify the existence of containers and images and get their varions ID
```sh
# list running containers
docker ps

# list all containers wherther running or in a stopped state
docker ps -a

# list all container images
docker images
```

#### Deleting containers and container images
```sh
# stop the container
docker stop <container_id>

# delete the container
docker rm <container_id>

# delete container image
docker rmi <image>
```

> For all CLI commands on Docker containers, reference the Docker documentation site https://docs.docker.com/reference/


### Adding DynamoDB Local and Postgres

Cruddur will utilize Postgres and DynamoDB for database. Equally, the creation process needs to be automated

#### Postgres
Add the following to the docker-compose.yml file under ``services``
```yaml
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
```

To install the postgres client into Gitpod

```sh
  - name: postgres
    init: |
      curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
      sudo apt update
      sudo apt install -y postgresql-client-13 libpq-dev
```

### DynamoDB Local
Also add the following to the docker-compose.yml file under ``services``
```yaml
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
```

Example of using DynamoDB local
https://github.com/100DaysOfCloud/challenge-dynamodb-local

## Volumes

directory volume mapping

```yaml
volumes: 
- "./docker/dynamodb:/home/dynamodblocal/data"
```

named volume mapping

```yaml
volumes: 
  - db:/var/lib/postgresql/data

volumes:
  db:
    driver: local
```
