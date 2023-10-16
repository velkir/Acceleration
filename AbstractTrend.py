from abc import ABC, abstractmethod


class AbstractTrend(ABC):
    def __init__(self, point0, point1):
        self.point0 = point0
        self.point1 = point1
        self.speed = self.calculate_speed()
        self.length = self.calculate_length()
        self.delta = self.calculate_delta()

    @abstractmethod
    def calculate_speed(self):
        pass

    @abstractmethod
    def calculate_length(self):
        pass

    @abstractmethod
    def calculate_delta(self):
        pass
