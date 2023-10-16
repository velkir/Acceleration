from AbstractDataWalker import AbstractDataWalker
from Config import Config
from Point import Point
from Structure import Structure
from Trend import Trend


class DataWalker(AbstractDataWalker):
    def __init__(self, ohlc_data, structure=None, current_trend=None):
        if structure is None:
            structure = Structure()
        super().__init__(structure=structure, ohlc_data=ohlc_data, current_trend=current_trend)
        self.current_index = 0

    def next(self):
        self.update_bar()
        if self.is_first_bar():
            self.analyze_first_bar()
        else:
            self.analyze_bar()

    def update_bar(self):
        self.current_index += 1
        self.current_bar = self.ohlc_data.iloc[self.current_index]

    def is_first_bar(self):
        return self.current_index == 1 and self.current_trend is None

    def analyze_first_bar(self):
        config = Config()
        point0_price = config.Point0.price
        point0_timestamp = config.Point0.timestamp
        point0_id = config.Point0.id
        self.current_trend = self.create_trend(point0=Point.create_point(price=point0_price,
                                                                         timestamp=point0_timestamp,
                                                                         id=point0_id),
                                               point1=Point.create_point(price=self.current_bar["low"],
                                                                         timestamp=self.current_bar['timestamp'],
                                                                         id=self.current_index))
        self.structure.add_trend(self.current_trend)

    def analyze_bar(self):
        #недописано
        analysis = self.compare_speed()
        # if analysis == ""

    def calculate_speed(self):
        pass

    def compare_speed(self):
        pass

    def create_trend(self, point0, point1):
        return Trend(point0=point0, point1=point1)


