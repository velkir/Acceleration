from abc import ABC, abstractmethod


class AbstractTrend(ABC):
    def __init__(self, point0, point1, parent_trend):
        self.point0 = point0
        self.point1 = point1
        self.speed = self.calculate_speed()
        self.length = self.calculate_length()
        self.delta = self.calculate_delta()
        self.subtrends = []
        self.parent_trend = parent_trend
        self.layer = parent_trend.layer + 1 if parent_trend is not None else 0
        self.status = 0

    @abstractmethod
    def calculate_speed(self):
        pass

    @abstractmethod
    def calculate_length(self):
        pass

    @abstractmethod
    def calculate_delta(self):
        pass
