import abc
from typing import List

from docker_compose_diagram.docker_compose.entities.service import DockerComposeService


class Plugin(abc.ABC):
    @abc.abstractmethod
    def execute(self, services: List[DockerComposeService], drawn_nodes: dict):
        raise NotImplementedError
