import click

from docker_compose_diagram.di_container.facade import docker_compose_parser, plugins
from docker_compose_diagram.di_container.terminal import terminal
from docker_compose_diagram.facade import DockerComposeDiagramFacade
from docker_compose_diagram.renderer.base import Renderer
from docker_compose_diagram.renderer.diagrams import DiagramsRenderer


def run(file, direction, nodesep, out_format):
    with terminal.status(name="Working.."):
        # Adapter. Renders final image using diagrams package
        renderer: Renderer = DiagramsRenderer(
            plugins=plugins,
            config={
                "direction": direction,
                "nodesep": nodesep,
                "out_format": out_format,
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


@click.command()
@click.option(
    "--file", default="docker-compose.yml", help="Path to docker-compose file"
)
@click.option(
    "--direction",
    default="TB",
    type=click.Choice(["TB", "BT", "LR", "RL"], case_sensitive=True),
)
@click.option("--nodesep", default="1.0", type=click.FLOAT)
@click.option(
    "--out-format",
    help="Save output file with the following format",
    default="png",
    type=click.Choice(["png", "jpg", "svg", "pdf", "dot"], case_sensitive=False),
)
def process_cli(file, direction, nodesep, out_format):
    run(file, direction, nodesep, out_format)


if __name__ == "__main__":
    process_cli()
