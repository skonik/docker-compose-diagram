import sys
from typing import Dict, Any

import yaml
from diagrams import Cluster, Diagram

from docker_compose_diagram.docker_compose.services import DockerComposeServiceStorage, DockerComposeService
from docker_compose_diagram.docker_images.utils import determine_diagram_render_class, determine_image_name


def collect_services_into_storage(
        docker_compose_parsed: Dict[str, Any],
) -> DockerComposeServiceStorage:
    diagram_nodes_storage = DockerComposeServiceStorage()
    for service_name, service_info in docker_compose_parsed["services"].items():
        image_name = determine_image_name(
            service_info=service_info,
        )
        render_class = determine_diagram_render_class(
            image_name=image_name,
        )

        docker_compose_service = DockerComposeService(
            name=service_name,
            service_info=service_info,
            diagram_render_class=render_class,
        )
        diagram_nodes_storage.add(service=docker_compose_service)

    return diagram_nodes_storage


def render_clustered_services(storage: DockerComposeServiceStorage) -> None:
    clusters: Dict = storage.group_by_cluster()
    for cluster_name, cluster_services in clusters.items():
        if cluster_name is None:
            continue

        with Cluster(cluster_name):
            for service in cluster_services:
                service.render()


def render_not_clustered_services(storage: DockerComposeServiceStorage) -> None:
    clusters: Dict = storage.group_by_cluster()
    not_clustered_services = clusters.pop(None, [])

    for service in not_clustered_services:
        service.render()


def render_dependencies(storage: DockerComposeServiceStorage):
    for service in storage.all():
        service.render_dependency_arrows(storage=storage)


def pars_yaml_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as stream:
        try:
            parsed_yaml_structure = yaml.safe_load(stream)
        except yaml.YAMLError:
            print('Failed to parse file')
            sys.exit()

    return parsed_yaml_structure


def draw(file, direction, graph_attr):
    docker_compose_parsed = pars_yaml_file(file_path=file)
    diagram_nodes_storage = collect_services_into_storage(docker_compose_parsed)

    with Diagram("docker-compose", show=False, direction=direction, graph_attr=graph_attr):
        with Cluster(file):
            render_clustered_services(storage=diagram_nodes_storage)
            render_not_clustered_services(storage=diagram_nodes_storage)
            render_dependencies(storage=diagram_nodes_storage)
