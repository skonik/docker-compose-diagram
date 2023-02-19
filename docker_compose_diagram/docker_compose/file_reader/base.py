import abc


class FileReader(abc.ABC):
    """This class is responsible for reading a docker-compose file."""

    @abc.abstractmethod
    def read(self, path: str) -> str:
        raise NotImplementedError
