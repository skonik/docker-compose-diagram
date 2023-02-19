from typing import List

import yaml

from docker_compose_diagram.docker_compose.entities.service import \
    DockerComposeService
from docker_compose_diagram.docker_compose.parser.base import \
    DockerComposeParser
from docker_compose_diagram.docker_images.utils import read_dockerfile_image


class YAMLBasedParser(DockerComposeParser):
    def parse(self, file_path: str) -> List[DockerComposeService]:
        content: str = self.file_reader.read(path=file_path)

        try:
            parsed_yaml_structure = yaml.safe_load(content)

            deserialized_services = []
            for service_name, service_definition in parsed_yaml_structure[
                "services"
            ].items():
                image_name = read_dockerfile_image(service_info=service_definition)

                service_entity = DockerComposeService(
                    name=service_name,
                    image=image_name,
                    labels=service_definition.get("labels", {}),
                    depends_on=service_definition.get("depends_on", []),
                )
                deserialized_services.append(service_entity)

            return deserialized_services

        except yaml.YAMLError:
            print("Failed to parse file")
            exit(0)
