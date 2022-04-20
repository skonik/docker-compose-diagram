import re
from os import path

from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SNS, SQS
from diagrams.generic.compute import Rack
from diagrams.onprem.database import PostgreSQL, MySQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import RabbitMQ
from diagrams.programming.language import Python, Ruby, Go
from dockerfile_parse import DockerfileParser

from .labels import process_labels

DEFAULT_ICON_CLASS = Rack


class ImageRenderer:
    pattern = r''
    diagram_class = None

    def render(self, service_name):
        return self.diagram_class(service_name)


class RedisImage(ImageRenderer):
    pattern = r'redis:'
    diagram_class = Redis


class PostgreSQLImage(ImageRenderer):
    pattern = r'postgres:'
    diagram_class = PostgreSQL


class NginxImage(ImageRenderer):
    pattern = r'nginx'
    diagram_class = Nginx


class PythonImage(ImageRenderer):
    pattern = r'python'
    diagram_class = Python


class MysqlImage(ImageRenderer):
    pattern = r'mysql'
    diagram_class = MySQL


class SNSImage(ImageRenderer):
    pattern = r'sns$'
    diagram_class = SNS


class SQSImage(ImageRenderer):
    pattern = r'sqs'
    diagram_class = SQS


class DynamoDBImage(ImageRenderer):
    pattern = r'dynamodb'
    diagram_class = Dynamodb


class RubbyImage(ImageRenderer):
    pattern = r'ruby'
    diagram_class = Ruby


class GolangImage(ImageRenderer):
    pattern = r'golang'
    diagram_class = Go


class RabbitMQImage(ImageRenderer):
    pattern = r'rabbitmq'
    diagram_class = RabbitMQ


drawn_services = dict()


def already_drawn(tracking_node):
    global drawn_services
    return tracking_node in drawn_services


def draw_dependency(source, goal):
    drawn_services[source] >> drawn_services[goal]


def read_dockerfile_image(service_info):
    build = service_info.get('build', {})
    context = build.get('context')
    if context is None:
        return None

    dockerfile_path = build.get('dockerfile')
    if dockerfile_path is None:
        dockerfile_path = path.join(context, 'Dockerfile')
    else:
        dockerfile_path = path.join(context, dockerfile_path)

    dfp = DockerfileParser()
    with open(dockerfile_path, 'r') as file:
        dfp.content = file.read()

    return dfp.baseimage


def render_image_icon(service_name, service_info):
    global drawn_services

    image_name = service_info.get('image')
    if image_name is None:
        image_name = read_dockerfile_image(service_info=service_info)

    image_from_label = process_labels(service_name=service_name, service_info=service_info)
    if image_from_label:
        drawn_services[service_name] = image_from_label
        return drawn_services[service_name]

    if image_name is None:
        icon_instance = DEFAULT_ICON_CLASS(service_name)
        drawn_services[service_name] = icon_instance
        return drawn_services[service_name]

    if service_name not in drawn_services.keys():

        for subclass in ImageRenderer.__subclasses__():
            re_match = re.search(subclass.pattern, image_name)
            if re_match:
                icon_instance = subclass().render(service_name=service_name)
                break
        else:
            icon_instance = DEFAULT_ICON_CLASS(
                service_name,
            )

        drawn_services[service_name] = icon_instance

    return drawn_services[service_name]
