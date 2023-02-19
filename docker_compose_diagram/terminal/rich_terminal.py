from typing import Any

from rich.console import Console

from docker_compose_diagram.terminal.base import Terminal

console = Console()


class RichTerminal(Terminal):
    def status_enter(self, name: str) -> Any:
        self.status = console.status(status=name)
        self.status.start()

        return self.status

    def status_exit(self, name: str) -> None:
        self.status.stop()

    def print(self, text: str, style: str = "") -> None:
        console.print(text, style=style)
