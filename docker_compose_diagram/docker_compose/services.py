from __future__ import annotations

from dataclasses import dataclass, field
from collections import defaultdict
from typing import List, Dict, Type, Any, Optional

from diagrams import Node

from docker_compose_diagram.docker_images.utils import determine_diagram_render_class

LABELS_PREFIX = 'docker_compose_diagram'
CLUSTER_LABEL_VALUE = f'{LABELS_PREFIX}.cluster'
ICON_LABEL_VALUE = f'{LABELS_PREFIX}.icon'
DESCRIPTION_LABEL_VALUE = f'{LABELS_PREFIX}.description'


@dataclass
class DockerComposeService:
    name: str
    service_info: Dict[str, Any]

    cluster: Optional[str] = None
    description: str = ''
    diagram_render_class: Type[Node] = None
    diagram_render_class_instance: Node = None

    def __post_init__(self):
        labels = self.service_info.get('labels', {})
        self.cluster = labels.get(CLUSTER_LABEL_VALUE)
        self.description = labels.get(DESCRIPTION_LABEL_VALUE, '')

        label_icon = labels.get(ICON_LABEL_VALUE)
        if isinstance(label_icon, str):
            self.diagram_render_class = determine_diagram_render_class(
                image_name=label_icon,
            )

    def render(self):
        self.diagram_render_class_instance = self.diagram_render_class(
            self.name +
            f'\n{self.description}',
        )
        return self.diagram_render_class_instance

    def render_dependency_arrows(self, storage: DockerComposeServiceStorage) -> None:
        for dependency_name in self.service_info.get('depends_on', []):
            dependency_service = storage.find_by_name(name=dependency_name)
            self.render_dependency_arrow(dependency=dependency_service)

    def render_dependency_arrow(self, dependency: DockerComposeService) -> None:
        return self.diagram_render_class_instance >> dependency.diagram_render_class_instance


@dataclass
class DockerComposeServiceStorage:
    docker_compose_services: Dict[str, DockerComposeService] = field(
        default_factory=dict,
    )

    def add(self, service: DockerComposeService) -> None:
        if service.name not in self.docker_compose_services.keys():
            self.docker_compose_services[service.name] = service

    def all(self) -> List[DockerComposeService]:
        return list(self.docker_compose_services.values())


    def group_by_cluster(self) -> Dict[str, List[DockerComposeService]]:
        cluster_name_to_services = defaultdict(list)
        for service in self.docker_compose_services.values():
            cluster_name_to_services[service.cluster].append(service)

        return cluster_name_to_services

    def find_by_name(self, name: str) -> DockerComposeService:
        return self.docker_compose_services[name]
