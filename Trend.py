from AbstractTrend import AbstractTrend


class Trend(AbstractTrend):
    def __init__(self, point0, point1, parent_trend=None):
        super().__init__(point0=point0, point1=point1, parent_trend=parent_trend)

    def calculate_speed(self):
        return (self.point1.price - self.point0.price) / (self.point1.id - self.point0.id)

    def calculate_length(self):
        pass

    def calculate_delta(self):
        pass

