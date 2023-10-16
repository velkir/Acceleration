from abc import ABC, abstractmethod


class AbstractOHLCDataMapper(ABC):
    @abstractmethod
    def map_data(self, raw_data):
        raise NotImplementedError("This function is not yet implemented.")
