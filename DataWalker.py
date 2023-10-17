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
            print("here")
        elif not self.is_first_bar() and self.is_second_bar():
            self.analyze_second_bar()
        else:
            self.analyze_bar()

        self.update_index()

    def update_bar(self):
        self.current_bar = self.ohlc_data.iloc[self.current_index]

    def update_index(self):
        self.current_index += 1

    def is_first_bar(self):
        return self.current_index == 0 and self.current_trend is None

    def is_second_bar(self):
        return self.current_index == 1 and self.current_trend is None

    def analyze_second_bar(self):
        config = Config()
        point0_price = config.Point0.price
        point0_timestamp = config.Point0.timestamp
        point0_id = config.Point0.id

        #инициализация первого тренда
        self.current_trend = self.create_trend(point0=Point.create_point(price=point0_price,
                                                                         timestamp=point0_timestamp,
                                                                         id=point0_id),
                                               point1=Point.create_point(price=self.current_bar["low"],
                                                                         timestamp=self.current_bar['timestamp'],
                                                                         id=self.current_index))
        self.structure.add_trend(self.current_trend)

    def analyze_bar(self):
        current_speed = self.current_trend.speed

        new_speed_point1 = Point.create_point(price=self.current_bar["low"],
                                              timestamp=self.current_bar["timestamp"],
                                              id=self.current_index)
        new_speed = self.calculate_speed(self.current_trend.point1, new_speed_point1)

        should_create_new, should_delete_current = self.compare_speed(current_speed, new_speed)

        if should_create_new:
            new_trend = self.create_trend(point0=self.current_trend.point1,
                                          point1=new_speed_point1,
                                          parent_trend=self.current_trend)
            self.current_trend.subtrends.append(new_trend)
            self.current_trend = new_trend

        if should_delete_current:
            if self.current_trend.parent_trend:
                self.current_trend.parent_trend.subtrends.remove(self.current_trend)
                self.assign_parent_trend_as_current_trend()
                self.analyze_bar()
            else:
                self.structure.delete_trend(self.current_trend)
                new_trend = self.create_trend(point0=self.current_trend.point0,
                                              point1=new_speed_point1,
                                              parent_trend=None)
                self.current_trend = new_trend
                self.structure.add_trend(self.current_trend)

    def calculate_speed(self, point0, point1):
        return (point1.price - point0.price) / (point1.id - point0.id)

    def compare_speed(self, current_speed, new_speed):
        #Если скорость нового тренда выше скорости текущего, то создаем новый тренд
        if new_speed > current_speed:
            return True, False
        else:
            return False, True

    def create_trend(self, point0, point1, parent_trend=None):
        return Trend(point0=point0, point1=point1, parent_trend=parent_trend)

    def assign_parent_trend_as_current_trend(self):
        self.current_trend = self.current_trend.parent_trend


