from abc import abstractmethod, ABC
import pandas as pd
from AbstractStructure import AbstractStructure
from AbstractTrend import AbstractTrend


class AbstractDataWalker(ABC):
    def __init__(self, structure: AbstractStructure, ohlc_data: pd.DataFrame, current_trend: AbstractTrend or None):
        self.structure = structure
        self.current_trend = current_trend
        self.ohlc_data = ohlc_data
        self.current_bar = self.ohlc_data.iloc[0]

    @abstractmethod
    def next(self):
        pass

