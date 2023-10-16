from abc import abstractmethod, ABC
from AbstractStructure import AbstractStructure
from AbstractTrend import AbstractTrend


class AbstractDataWalker(ABC):
    def __init__(self, structure: AbstractStructure, current_trend: AbstractTrend or None):
        self.structure = structure
        self.current_trend = current_trend

    @abstractmethod
    def next(self):
        pass
