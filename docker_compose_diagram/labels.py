import re

from diagrams.aws.storage import S3
from diagrams.onprem.queue import Celery
from diagrams.programming.framework import Django, Flask


class Label:
    key = 'docker_compose_diagram.icon'
    pattern = r''
    diagram_class = None

    def render(self, service_name):
        return self.diagram_class(service_name)


class DjangoLabel(Label):
    pattern = r'django'
    diagram_class = Django


class CeleryLabel(Label):
    pattern = r'celery'
    diagram_class = Celery


class FastAPI(Label):
    pattern = r'flask'
    diagram_class = Flask


class S3Label(Label):
    pattern = r's3'
    diagram_class = S3


def process_labels(service_name, service_info):
    labels = service_info.get('labels', {})
    if Label.key in labels:
        for subclass in Label.__subclasses__():
            if re.search(subclass.pattern, labels[Label.key]):
                return subclass().render(service_name=service_name)

    return None
