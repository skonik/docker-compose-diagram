import abc
from typing import Any, Dict, List

from docker_compose_diagram.docker_compose.entities.service import \
    DockerComposeService
from docker_compose_diagram.renderer.plugins.base import Plugin


class Renderer(abc.ABC):
    def __init__(
        self,
        plugins: List[Plugin] = None,
        config: Dict[str, Any] = None,
    ) -> None:
        if plugins is None:
            plugins = []

        if config is None:
            config = {}

        self.plugins = plugins
        self.config = config

    @abc.abstractmethod
    def render(
        self,
        services: List[DockerComposeService],
        destination_file: str,
    ) -> None:
        raise NotImplementedError
