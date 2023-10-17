class Serializer:
    def trend_to_dict(self, trend):
        return {
            'point0': self.point_to_dict(trend.point0),
            'point1': self.point_to_dict(trend.point1),
            'speed': trend.speed,
            'length': trend.length,
            'delta': trend.delta,
            'subtrends': [self.trend_to_dict(subtrend) for subtrend in trend.subtrends],
            'layer': trend.layer,
            'status': trend.status
        }

    def point_to_dict(self, point):
        return {
            'price': point.price,
            'timestamp': point.timestamp,
            'id': point.id
        }

    def structure_to_dict(self, structure):
        return {
            'structure': [self.trend_to_dict(trend) for trend in structure.structure],
            'length': structure.length
        }
