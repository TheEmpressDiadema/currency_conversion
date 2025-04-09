from typing import Protocol
from abc import abstractmethod

class IDao(Protocol):

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass