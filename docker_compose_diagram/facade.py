from docker_compose_diagram.docker_compose.parser.base import \
    DockerComposeParser
from docker_compose_diagram.renderer.base import Renderer


class DockerComposeDiagramFacade:
    """Application Facade."""

    def __init__(
        self,
        docker_compose_parser: DockerComposeParser,
        renderer: Renderer,
    ) -> None:
        self.docker_compose_parser = docker_compose_parser
        self.renderer = renderer

    def draw(self, source_file: str, destination_file: str) -> None:
        services = self.docker_compose_parser.parse(
            file_path=source_file,
        )
        self.renderer.render(
            services=services,
            destination_file=destination_file,
        )
