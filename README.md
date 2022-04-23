# docker-compose-diagram
Script drawing a diagram of your docker-compose file

## Installation

Please install [graphviz](https://graphviz.gitlab.io/download/).
Then install this util from pypi via pip or other package manager.
```
pip install docker-compose-diagram
```

## Usage

```sh
$ compose-diagram --file docker-compose.yml --direction=TB --nodesep=1.2
```


## Example

Let's say we have the following docker-compose file:

```yaml
version: "3.8"

services:

  backend-api:
    build:
      context: ..
      dockerfile: docker/django/Dockerfile
    image: dev_backend
    container_name: dev_backend
    restart: always
    volumes:
      - ..:/app/
    depends_on:
      - db
      - redis
      - dynamodb
      - sns
      - s3_minio
    working_dir: "/app/backend"
    expose:
      - 8000
    ports:
      - "8000:8000"
    command: runserver
    labels:
      "docker_compose_diagram.icon": "django"


  db:
    container_name: backend_api_db
    image: mysql/mysql-server:8
    volumes:
      - mysql_data:/var/lib/mysql
    restart: unless-stopped
    ports:
      - "3306:3306"


  s3_minio:
    image: minio/minio:latest
    container_name: dev_minio
    entrypoint: sh
    command: -c 'minio server /data  --console-address ":9001"'
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - ./minio_data:/data
    labels:
      "docker_compose_diagram.icon": "s3"


  celery-worker:
    container_name: dev_celery_worker
    build:
      context: ..
      dockerfile: docker/django/Dockerfile
    image: dev_backend
    working_dir: /app/backend
    volumes:
      - ..:/app/
    command: celery -A config worker  --autoscale=8,1 -P gevent -l INFO
    restart: unless-stopped
    depends_on:
      - db
      - sqs
    labels:
      "docker_compose_diagram.icon": "celery"


  celery-beat:
    container_name: dev_celery_beat
    build:
      context: ..
      dockerfile: docker/django/Dockerfile
    image: dev_backend
    working_dir: /app/backend
    volumes:
      - ..:/app/
    command: celery -A config beat  -l INFO
    restart: unless-stopped
    depends_on:
      - db
      - sqs
    labels:
      "docker_compose_diagram.icon": "celery"

  sqs:
    image: roribio16/alpine-sqs
    ports:
      - 9324:9324
      - 9325:9325
    volumes:
      - ./sqs/elasticmq.conf:/opt/config/elasticmq.conf


  dynamodb:
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
    image: "amazon/dynamodb-local:latest"
    container_name: dev_dynamodb
    ports:
      - "11000:8000"
    volumes:
      - "./dynamodb:/home/dynamodblocal/data"
    working_dir: /home/dynamodblocal

  sns:
    image: s12v/sns
    container_name: dev_sns
    ports:
      - "9911:9911"
    depends_on:
      - sqs

  redis:
    image: redis:alpine
    container_name: dev_redis
    restart: unless-stopped
    ports:
      - "6379:6379"

volumes:
  mysql_data:

```

will create the following `.png` file
![docker-compose.png](./examples/docker-compose.png)

## Use cases

* project documentation;
* catching dependencies bugs in your docker-compose file;

