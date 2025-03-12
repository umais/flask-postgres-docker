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
git clone https://github.com/your-username/flask-postgres-docker.git
cd flask-postgres-docker

```
### 2. Configure the .env File
Create a .env file in the root directory to store sensitive information (like passwords and database names).

```bash
touch .env


DB_HOST=flaskapi_postgresql
DB_NAME=flaskapi_db
DB_USER=admin
DB_PASS=Express1234%
POSTGRES_USER=admin
POSTGRES_PASSWORD=Express1234%
POSTGRES_DB=flaskapi_db

echo ".env" >> .gitignore
```