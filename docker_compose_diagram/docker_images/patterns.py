from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SNS, SQS
from diagrams.aws.storage import S3
from diagrams.generic.compute import Rack
from diagrams.onprem.database import PostgreSQL, MySQL, Mongodb
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Nginx, Traefik, Caddy
from diagrams.onprem.queue import Celery, Kafka
from diagrams.onprem.queue import RabbitMQ
from diagrams.programming.framework import Django, Flask, Rails, React, Vue, FastAPI
from diagrams.programming.language import (
    Python,
    Ruby,
    Go,
    Rust,
    Kotlin,
    Javascript,
    NodeJS,
)

DEFAULT_ICON_CLASS = Rack


class DockerImagePattern:
    pattern = r''
    diagram_render_class = None

    def render(self, service_name):
        return self.diagram_render_class(service_name)


class RedisImage(DockerImagePattern):
    pattern = r'redis:'
    diagram_render_class = Redis


class PostgreSQLImage(DockerImagePattern):
    pattern = r'postgres:'
    diagram_render_class = PostgreSQL


class NginxImage(DockerImagePattern):
    pattern = r'nginx'
    diagram_render_class = Nginx


class PythonImage(DockerImagePattern):
    pattern = r'python'
    diagram_render_class = Python


class MysqlImage(DockerImagePattern):
    pattern = r'mysql'
    diagram_render_class = MySQL


class SNSImage(DockerImagePattern):
    pattern = r'sns$'
    diagram_render_class = SNS


class SQSImage(DockerImagePattern):
    pattern = r'sqs'
    diagram_render_class = SQS


class DynamoDBImage(DockerImagePattern):
    pattern = r'dynamodb'
    diagram_render_class = Dynamodb


class RubbyImage(DockerImagePattern):
    pattern = r'ruby'
    diagram_render_class = Ruby


class GolangImage(DockerImagePattern):
    pattern = r'golang'
    diagram_render_class = Go


class RabbitMQImage(DockerImagePattern):
    pattern = r'rabbitmq'
    diagram_render_class = RabbitMQ


class DjangoImage(DockerImagePattern):
    pattern = r'django'
    diagram_render_class = Django


class CeleryImage(DockerImagePattern):
    pattern = r'celery'
    diagram_render_class = Celery


class FlaskImage(DockerImagePattern):
    pattern = r'flask'
    diagram_render_class = Flask


class S3Image(DockerImagePattern):
    pattern = r's3'
    diagram_render_class = S3


class RailsImage(DockerImagePattern):
    pattern = r'rails'
    diagram_render_class = Rails


class RustImage(DockerImagePattern):
    pattern = r'rust'
    diagram_render_class = Rust


class KotlinImage(DockerImagePattern):
    pattern = r'kotlin'
    diagram_render_class = Kotlin


class NodeJSImage(DockerImagePattern):
    pattern = r'node'
    diagram_render_class = NodeJS


class JavaScriptImage(DockerImagePattern):
    pattern = r'javascript'
    diagram_render_class = Javascript


class MongodbImage(DockerImagePattern):
    pattern = r'mongo'
    diagram_render_class = Mongodb


class ReactImage(DockerImagePattern):
    pattern = r'react'
    diagram_render_class = React


class VueImage(DockerImagePattern):
    pattern = r'vue'
    diagram_render_class = Vue


class KafkaImage(DockerImagePattern):
    pattern = r'kafka'
    diagram_render_class = Kafka


class TraefikImage(DockerImagePattern):
    pattern = r'traefik'
    diagram_render_class = Traefik


class CaddyImage(DockerImagePattern):
    pattern = r'caddy'
    diagram_render_class = Caddy


class FastAPIImage(DockerImagePattern):
    pattern = r'fastapi'
    diagram_render_class = FastAPI
