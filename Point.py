class Point:
    """Модель точки. Id точки = Id бара. Нужен для быстрого вычисления length у элементов"""
    def __init__(self, price: float, timestamp, id: int):
        self.price = price
        self.timestamp = timestamp
        self.id = id

    @staticmethod
    def create_point(price, timestamp, id):
        return Point(price, timestamp, id)
