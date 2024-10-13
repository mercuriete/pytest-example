from abc import abstractmethod


class HelloWorld:
    @abstractmethod
    def getString(self) -> str:
        pass
