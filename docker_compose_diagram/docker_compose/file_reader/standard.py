import os

from docker_compose_diagram.di_container.terminal import terminal
from docker_compose_diagram.docker_compose.constants import messages
from docker_compose_diagram.docker_compose.file_reader.base import FileReader


class StandardFileReader(FileReader):
    """Standard library file reader implementation."""

    def read(self, path: str) -> str:
        if not os.path.exists(path=path):
            message = messages.FILE_NOT_FOUND.format(filename=path)
            terminal.print(text=message, style="red")
            exit(code=1)

        message = messages.FILE_FOUND.format(filename=path)
        terminal.print(text=message, style="green")

        with open(file=path, mode="r") as file:
            return file.read()
