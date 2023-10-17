from AbstractDataWalker import AbstractDataWalker
from BarAnalyzer import BarAnalyzer
from Config import Config
from Point import Point
from StatusManager import StatusManager
from Structure import Structure
from Trend import Trend
from TrendManager import TrendManager


class DataWalker(AbstractDataWalker):
    def __init__(self, ohlc_data, structure=None, current_trend=None):
        if structure is None:
            structure = Structure()
        super().__init__(structure=structure, ohlc_data=ohlc_data, current_trend=current_trend)
        self.current_index = 0
        self.config = Config()
        self.status_manager = StatusManager(self)
        self.bar_analyzer = BarAnalyzer(self)
        self.trend_manager = TrendManager(self)

    def next(self):
        #взятие следующего бара
        self.update_bar()

        #действие в зависимости от того 1, 2 или 3 сейчас бар
        self.bar_analyzer.analyze_bar_based_on_index()
        #меняет статус текущего тренда и всех его родителей, если выполняется условие (самое простое - текущий слой)
        self.status_manager.check_and_change_status()
        self.update_index()

    def update_bar(self):
        self.current_bar = self.ohlc_data.iloc[self.current_index]

    def update_index(self):
        self.current_index += 1

    def initialize_first_bar(self):
        pass

    def analyze_second_bar(self):
        self.initialize_trend_from_config()

    def initialize_trend_from_config(self):
        point0 = Point.create_point(price=self.config.Point0.price,
                                    timestamp=self.config.Point0.timestamp,
                                    id=self.config.Point0.id)
        point1 = Point.create_point(price=self.current_bar["low"],
                                    timestamp=self.current_bar['timestamp'],
                                    id=self.current_index)
        self.current_trend = self.create_trend(point0, point1)
        self.structure.add_trend(self.current_trend)

    def analyze_general_bar(self):
        self.trend_manager.analyze_general_bar()

    def create_trend(self, point0, point1, parent_trend=None):
        return Trend(point0=point0, point1=point1, parent_trend=parent_trend)
