import abc
from contextlib import contextmanager


class Terminal(abc.ABC):
    """Terminal wrapper for pringint variouse info."""

    @contextmanager
    def status(self, name: str):
        status = self.status_enter(name=name)
        yield status
        self.status_exit(name=name)

    @abc.abstractmethod
    def status_enter(self, name: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def status_exit(self, name: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def print(self, text: str, style: str = "") -> None:
        raise NotImplementedError
