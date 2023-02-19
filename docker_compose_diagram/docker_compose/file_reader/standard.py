from docker_compose_diagram.docker_compose.file_reader.base import FileReader


class StandardFileReader(FileReader):
    """Standard library file reader implementation."""

    def read(self, path: str) -> str:
        with open(file=path, mode="r") as file:
            return file.read()
