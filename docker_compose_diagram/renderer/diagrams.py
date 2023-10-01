from typing import List

from diagrams import Cluster, Diagram

from docker_compose_diagram.di_container.terminal import terminal
from docker_compose_diagram.docker_compose.entities.service import DockerComposeService
from docker_compose_diagram.renderer.base import Renderer
from docker_compose_diagram.renderer.constants import messages


class DiagramsRenderer(Renderer):
    DRAWN_NODES = {}

    def render(
        self,
        services: List[DockerComposeService],
        destination_file: str,
    ) -> None:
        out_format = self.config.get("out_format", "png")

        with Diagram(
            destination_file,
            show=False,
            direction=self.config.get("direction", "TB"),
            graph_attr={
                "nodesep": str(self.config.get("nodesep", "1.0")),
            },
            outformat=out_format,
        ):
            with Cluster("docker-compose"):
                for plugin in self.plugins:
                    plugin.execute(services, self.DRAWN_NODES)

        message = messages.FILE_SAVED.format(
            filename=destination_file,
            out_format=out_format,
        )
        terminal.print(text=message, style="green")
