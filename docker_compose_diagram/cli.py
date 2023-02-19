import click

from docker_compose_diagram.docker_compose.file_reader.base import FileReader
from docker_compose_diagram.docker_compose.file_reader.standard import \
    StandardFileReader
from docker_compose_diagram.docker_compose.parser.base import \
    DockerComposeParser
from docker_compose_diagram.docker_compose.parser.yaml import YAMLBasedParser
from docker_compose_diagram.facade import DockerComposeDiagramFacade
from docker_compose_diagram.renderer.base import Renderer
from docker_compose_diagram.renderer.diagrams import DiagramsRenderer
from docker_compose_diagram.renderer.plugins.diagrams import (
    ClusteredNodesDrawer, DependenciesArrayDrawer, NotClusteredNodesDrawer)


@click.command()
@click.option("--file", default="docker-compose.yml", help="docker-compose file")
@click.option(
    "--direction",
    default="TB",
    type=click.Choice(["TB", "BT", "LR", "RL"], case_sensitive=True),
)
@click.option("--nodesep", default="1.0", type=click.FLOAT)
def process_cli(file, direction, nodesep):
    # Prepare adapters such as file reader, parser and renderer.
    # FileReader adapter reads files. StandardFileReader uses os.open
    file_reader: FileReader = StandardFileReader()

    # Parser adapter. Parses docker-compose.yml using yaml parser
    docker_compose_parser: DockerComposeParser = YAMLBasedParser(
        file_reader=file_reader,
    )

    # Plugins for renderer adapter. Order is important
    # Plugins represent steps of drawing.
    plugins = [
        # Draw node icons of clustered services first
        ClusteredNodesDrawer(),
        # Draw node icons of the rest
        NotClusteredNodesDrawer(),
        # Draw connections between services
        DependenciesArrayDrawer(),
    ]
    # Adapter. Renders final image using diagrams package
    renderer: Renderer = DiagramsRenderer(
        plugins=plugins,
        config={
            "direction": direction,
            "nodesep": nodesep,
        },
    )

    # Main application facade.
    # Uses all components to draw diagram
    app = DockerComposeDiagramFacade(
        docker_compose_parser=docker_compose_parser,
        renderer=renderer,
    )
    app.draw(
        source_file=file,
        destination_file="docker-compose",
    )


if __name__ == "__main__":
    process_cli()
