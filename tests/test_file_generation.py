import os.path

from docker_compose_diagram import cli


DOCKER_COMPOSE_FILE = "tests/docker-compose.dev.yml"
NEW_FILE = "docker-compose.png"


def test_file_created_after_running_cli():
    cli.run(DOCKER_COMPOSE_FILE, "TB", 1.2)
    assert os.path.exists(NEW_FILE)

    os.remove(NEW_FILE)
