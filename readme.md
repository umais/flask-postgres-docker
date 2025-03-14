# Flask App with PostgreSQL - Dockerized

This project is a simple Flask application connected to a PostgreSQL database, all running inside Docker containers. This README provides all the necessary commands and instructions for setting up the project locally.

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Project Setup

Follow these steps to get the project up and running.

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/umais/flask-postgres-docker.git
cd flask-postgres-docker

```
### 2. Configure the .env File
Create a .env file in the root directory to store sensitive information (like passwords and database names).

```bash
touch .env

```
Add the following variables to the .env file:

```bash
DB_HOST=flaskapi_postgresql
DB_NAME=flaskapi_db
DB_USER=admin
DB_PASS=Welcome1234%
POSTGRES_USER=admin
POSTGRES_PASSWORD=Welcome1234%
POSTGRES_DB=flaskapi_db
```
**Note:** Be sure to replace the passwords and other sensitive data with your own values. Do not commit this file to version control. Add .env to your .gitignore to prevent it from being pushed to GitHub.

```bash
echo ".env" >> .gitignore
```

### 3. Build and Start the Containers

Once the .env file is set up, use Docker Compose to build and start the containers:

```bash

docker-compose up -d --build

```

This command does the following:

Builds the Flask application image.

Starts the Flask app and PostgreSQL containers.

Initializes the database using init.sql if it's the first time the database is being set up.

### 4. Accessing the Application

After the containers are up and running, the Flask app should be accessible at:

```bash

http://localhost:5000
```

You can test the app by visiting the root endpoint to see a welcome message and confirm that Flask is running properly.

### 5. Stopping the Containers

To stop the containers, run:

```bash
docker-compose down

```

This will stop and remove the containers, but the data in the PostgreSQL container will persist because it's stored in a Docker volume (pgdata).

### 6. Removing All Containers and Volumes

To remove all containers and volumes (including PostgreSQL data), run:

```bash

docker-compose down -v
```


### 7. Useful Docker Commands

List all running containers:

```bash

docker ps

```
View logs of a specific container (e.g., flask_app):

```bash

docker logs flask_app

```
Access the Flask app container's shell:

```bash

docker exec -it flask_app bash

```

Access the PostgreSQL container's shell:

```bash

docker exec -it flaskapi_postgresql bash

```


Access the PostgreSQL CLI:

```bash

psql -U admin -d flaskapi_db



```

Get All Tables POSTGRESQL

```bash
SELECT * FROM information_schema.tables 
WHERE table_schema = 'public';

```

Get All Objects

```bash
SELECT * FROM pg_catalog.pg_class;

SELECT * FROM pg_indexes 
WHERE schemaname = 'public';

```

Reset Container Database & Some debugging options

```bash

docker-compose down -v  # -v removes associated volumes only use when want to recreate database
docker builder prune   # delete all cache
docker-compose up -d
docker logs <container_id>
```

### Endpoints

GET /
Returns a welcome message indicating that Flask is running inside a Docker container.

GET /users
Fetches all users from the database.

POST /users
Adds a new user to the database. The request body should include UserName, email, and password.

# DOCKER-COMPOSE COMMON KEYWORDS

 Summary of Common Keywords

version: Docker Compose file format version.

services: Define containers (most important section).

image: Specifies an image to use for a service.

build: Specifies how to build an image for the service.

ports: Maps container ports to host ports.

depends_on: Ensures the start order of services.

environment: Defines environment variables for a container.

volumes: Mounts volumes into a container.

command: Overrides the default command in the container.

restart: Configures automatic container restart behavior.

healthcheck: Defines how to check if a container is healthy.

networks: Defines networks for container communication.

extra_hosts: Adds custom entries to /etc/hosts.

logging: Configures logging for services.

deploy: Configures deployment settings for Docker Swarm.

args: Defines build-time arguments.

🔑 Summary of Key Differences between Dockerfile and Docker Compose File
Aspect	Dockerfile	docker-compose.yml
Purpose	Defines how to build an image	Defines how to run multiple containers (services)
Scope	Single container configuration	Multiple containers and their relationships
Focus	Building the image (install dependencies, copy files)	Service orchestration (networking, volumes, environment)
Common Keywords	FROM, RUN, CMD, COPY, EXPOSE, ENV, USER	services, image, build, ports, depends_on, volumes
Service Definition	Defines the setup for a single container	Defines multiple services (each corresponding to a container)
Networking	No networking configurations	Configures networks for communication between services
Persistent Data	No built-in volume management	Defines volumes to persist data across container restarts