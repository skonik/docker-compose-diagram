import re
from os import path
from typing import Any, Dict, Optional, Type, Union

from diagrams import Node
from diagrams.generic.compute import Rack
from dockerfile_parse import DockerfileParser

from docker_compose_diagram.docker_images.patterns import DockerImagePattern

DEFAULT_ICON_CLASS = Rack


def read_dockerfile_image(service_info):
    image = service_info.get("image")
    if image is not None:
        return image

    build = service_info.get("build", {})
    context = build.get("context")
    if context is None:
        return None

    dockerfile_path = build.get("dockerfile")
    if dockerfile_path is None:
        dockerfile_path = path.join(context, "Dockerfile")
    else:
        dockerfile_path = path.join(context, dockerfile_path)

    dfp = DockerfileParser()
    with open(dockerfile_path, "r") as file:
        dfp.content = file.read()

    return dfp.baseimage


def determine_image_name(
    service_info: Dict[str, Any],
) -> Optional[str]:
    image_name = service_info.get("image")
    if image_name is None:
        image_name = read_dockerfile_image(service_info=service_info)

    return image_name


def determine_diagram_render_class(
    image_name: str,
) -> Union[Type[DockerImagePattern], Type[Node]]:
    if image_name is None:
        return DEFAULT_ICON_CLASS

    for subclass in DockerImagePattern.__subclasses__():
        re_match = re.search(subclass.pattern, image_name)
        if re_match:
            return subclass.diagram_render_class

    return DEFAULT_ICON_CLASS
