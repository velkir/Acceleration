from abc import ABC, abstractmethod


class OHLCDataSource(ABC):
    @abstractmethod
    def get_raw_ohlc_data(self, path):
        raise NotImplementedError("This function is not yet implemented.")
