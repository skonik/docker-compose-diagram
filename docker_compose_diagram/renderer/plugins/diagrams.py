from typing import List

from diagrams import Cluster, Node

from docker_compose_diagram.docker_compose.entities.service import (
    DockerComposeService, ServiceSelector)
from docker_compose_diagram.docker_images.utils import \
    determine_diagram_render_class
from docker_compose_diagram.renderer.plugins.base import Plugin


def draw_service(service: DockerComposeService) -> Node:
    if service.icon_name is None:
        image_name = service.image
    else:
        image_name = service.icon_name

    diagram_node_image_class = determine_diagram_render_class(
        image_name=image_name,
    )

    text_under_service = f"{service.name}\n{service.description}"
    node_instance = diagram_node_image_class(text_under_service)

    return node_instance


class NotClusteredNodesDrawer(Plugin):
    def execute(
        self,
        services: List[DockerComposeService],
        drawn_nodes: dict,
    ) -> None:
        services_selector = ServiceSelector()
        services_selector.add(services=services)

        services = services_selector.retrieve_not_clustered()

        for service in services:
            node_instance = draw_service(service=service)
            drawn_nodes[service.name] = node_instance


class DependenciesArrayDrawer:
    def render_dependency_arrows(
        self, origin, depends_on: List[str], drawn_nodes
    ) -> None:
        for dependency_name in depends_on:
            dependency_node = drawn_nodes[dependency_name]
            self.render_dependency_arrow(origin=origin, destination=dependency_node)

    def render_dependency_arrow(self, origin, destination) -> None:
        return origin >> destination

    def execute(self, services: List[DockerComposeService], drawn_nodes: dict) -> None:
        for service in services:
            if service.name not in drawn_nodes:
                node_instance = draw_service(service=service)
                drawn_nodes[service.name] = node_instance

            node = drawn_nodes[service.name]
            self.render_dependency_arrows(node, service.depends_on, drawn_nodes)


class ClusteredNodesDrawer(Plugin):
    def execute(
        self,
        services: List[DockerComposeService],
        drawn_nodes: dict,
    ) -> None:

        services_selector = ServiceSelector()
        services_selector.add(services=services)

        services_selector.group_by_cluster()

        for cluster_name, services in services_selector.group_by_cluster().items():
            with Cluster(cluster_name):
                for service in services:
                    node_instance = draw_service(service=service)
                    drawn_nodes[service.name] = node_instance
