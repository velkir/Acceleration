from abc import ABC, abstractmethod


class AbstractStructure(ABC):
    def __init__(self, structure):
        self.structure = structure if structure is not None else []
        self.substructure = []

    @abstractmethod
    def add_trend(self, trend):
        pass

    @property
    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def get_current_trend_layer(self):
        pass

