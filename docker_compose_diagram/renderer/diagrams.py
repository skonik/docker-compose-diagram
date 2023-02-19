from typing import List

from diagrams import Cluster, Diagram

from docker_compose_diagram.docker_compose.entities.service import \
    DockerComposeService
from docker_compose_diagram.renderer.base import Renderer


class DiagramsRenderer(Renderer):
    DRAWN_NODES = {}

    def render(
        self,
        services: List[DockerComposeService],
        destination_file: str,
    ) -> None:
        with Diagram(
            destination_file,
            show=False,
            direction=self.config.get("direction", "TB"),
            graph_attr={
                "nodesep": str(self.config.get("nodesep", "1.0")),
            },
        ):
            with Cluster("docker-compose"):
                for plugin in self.plugins:
                    plugin.execute(services, self.DRAWN_NODES)
