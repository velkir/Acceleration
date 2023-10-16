from abc import ABC, abstractmethod


class AbstractStructure(ABC):
    def __init__(self, structure):
        self.structure = structure
        self.substructure = []

    @abstractmethod
    def add_trend(self, trend):
        pass

    @abstractmethod
    @property
    def length(self):
        pass

    @abstractmethod
    def get_current_trend_layer(self):
        pass
