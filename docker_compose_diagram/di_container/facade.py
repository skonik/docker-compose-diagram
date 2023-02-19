""" This file holds dependencies for main facade. """
from docker_compose_diagram.docker_compose.file_reader.base import FileReader
from docker_compose_diagram.docker_compose.file_reader.standard import \
    StandardFileReader
from docker_compose_diagram.docker_compose.parser.base import \
    DockerComposeParser
from docker_compose_diagram.docker_compose.parser.yaml import YAMLBasedParser
from docker_compose_diagram.renderer.plugins.diagrams import (
    ClusteredNodesDrawer, DependenciesArrayDrawer, NotClusteredNodesDrawer)

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
