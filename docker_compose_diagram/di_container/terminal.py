""" This file holds dependencies for terminal. """
from docker_compose_diagram.terminal.base import Terminal
from docker_compose_diagram.terminal.rich_terminal import RichTerminal

terminal: Terminal = RichTerminal()
