import sys

import click
import yaml
from diagrams import Cluster, Diagram

from compose_diagram.images import render_image_icon, already_drawn, draw_dependency


@click.command()
@click.option('--file', default='docker-compose.yml', help='docker-compose file')
@click.option('--direction', default="TB", type=click.Choice(["TB", "BT", "LR", "RL"], case_sensitive=True))
def main(file, direction):
    with open(file, 'r') as stream:
        try:
            doc = yaml.load(stream)
        except yaml.YAMLError:
            print('Failed to parse file')
            sys.exit()

        services = doc["services"]

        with Diagram("docker-compose", show=False, direction=direction):

            with Cluster(file):
                for service, service_info in services.items():
                    if not already_drawn(service):
                        render_image_icon(service_name=service, service_info=service_info)

                for current_service_name, service_info in services.items():
                    dependencies = services[current_service_name].get('depends_on', [])
                    for dependency_name in dependencies:
                        draw_dependency(source=current_service_name, goal=dependency_name)


if __name__ == '__main__':
    main()
