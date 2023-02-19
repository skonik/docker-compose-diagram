import abc
from typing import List

from docker_compose_diagram.docker_compose.entities.service import \
    DockerComposeService
from docker_compose_diagram.docker_compose.file_reader.base import FileReader


class DockerComposeParser(abc.ABC):
    """
    Inherit this class to implement docker-compose.yaml parser.
    Its responsibility is to transform yaml content into dict.
    """

    def __init__(self, file_reader: FileReader) -> None:
        self.file_reader = file_reader

    @abc.abstractmethod
    def parse(self, file_path: str) -> List[DockerComposeService]:
        raise NotImplementedError
