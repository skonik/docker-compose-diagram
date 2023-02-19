from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from docker_compose_diagram.docker_compose.constants.labels import Label

# Typing Aliases
Cluster = str


@dataclass
class DockerComposeService:
    """Represents service defined in docker-compose file."""

    name: str
    image: str
    labels: Dict[str, Any]
    depends_on: List[str]

    icon_name: str = ""
    cluster: Optional[str] = None
    description: str = ""

    def __post_init__(self):
        self.icon_name = self.labels.get(Label.ICON_LABEL_VALUE, self.image)
        self.cluster = self.labels.get(Label.CLUSTER_LABEL_VALUE)
        self.description = self.labels.get(Label.DESCRIPTION_LABEL_VALUE, "")


@dataclass
class ServiceSelector:
    """Helper class to filter docker compose services."""

    docker_compose_services: Dict[str, DockerComposeService] = field(
        default_factory=dict,
    )

    def add(self, services: List[DockerComposeService]) -> None:
        for service in services:
            if service.name not in self.docker_compose_services.keys():
                self.docker_compose_services[service.name] = service

    def all(self) -> List[DockerComposeService]:
        return list(self.docker_compose_services.values())

    def group_by_cluster(self) -> Dict[Cluster, List[DockerComposeService]]:
        cluster_name_to_services = defaultdict(list)
        for service in self.docker_compose_services.values():
            cluster_name_to_services[service.cluster].append(service)

        cluster_name_to_services.pop(None, None)

        return cluster_name_to_services

    def retrieve_not_clustered(self) -> List[DockerComposeService]:
        clustered = self.group_by_cluster()

        return clustered.get(None, [])

    def find_by_name(self, name: str) -> DockerComposeService:
        return self.docker_compose_services[name]
