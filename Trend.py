from AbstractTrend import AbstractTrend


class Trend(AbstractTrend):
    def __init__(self, point0, point1):
        super().__init__(point0=point0, point1=point1)

    def calculate_speed(self):
        pass

    def calculate_length(self):
        pass

    def calculate_delta(self):
        pass

