from Point import Point


class TrendManager:
    def __init__(self, data_walker):
        self.data_walker = data_walker

    def analyze_general_bar(self):
        current_speed = self.data_walker.current_trend.speed
        new_speed_point1 = self.create_new_speed_point1()
        new_speed = self.calculate_speed(self.data_walker.current_trend.point1, new_speed_point1)
        should_create_new, should_delete_current = self.compare_speed(current_speed, new_speed)

        self.process_trend_creation_or_deletion(should_create_new, should_delete_current, new_speed_point1)

    def create_new_speed_point1(self):
        return Point.create_point(price=self.data_walker.current_bar["low"],
                                  timestamp=self.data_walker.current_bar["timestamp"],
                                  id=self.data_walker.current_index)

    def process_trend_creation_or_deletion(self, should_create_new, should_delete_current, new_speed_point1):
        if should_create_new:
            self.create_and_assign_new_trend(new_speed_point1)
        if should_delete_current:
            self.delete_or_modify_current_trend(new_speed_point1)

    def create_and_assign_new_trend(self, new_speed_point1):
        new_trend = self.data_walker.create_trend(self.data_walker.current_trend.point1, new_speed_point1, self.data_walker.current_trend)
        self.data_walker.current_trend.subtrends.append(new_trend)
        self.data_walker.current_trend = new_trend

    def delete_or_modify_current_trend(self, new_speed_point1):
        if self.data_walker.current_trend.parent_trend:
            self.delete_or_modify_child_trend()
        else:
            self.delete_or_replace_root_trend(new_speed_point1)

    def delete_or_modify_child_trend(self):
        if self.data_walker.current_trend.status == 0:
            self.data_walker.current_trend.parent_trend.subtrends.remove(self.data_walker.current_trend)
        self.data_walker.current_trend = self.data_walker.current_trend.parent_trend
        self.analyze_general_bar()

    def delete_or_replace_root_trend(self, new_speed_point1):
        if self.data_walker.current_trend.status == 0:
            self.data_walker.structure.delete_trend(self.data_walker.current_trend)
        new_trend = self.data_walker.create_trend(self.data_walker.current_trend.point0, new_speed_point1)
        self.data_walker.current_trend = new_trend
        self.data_walker.structure.add_trend(self.data_walker.current_trend)

    def calculate_speed(self, point0, point1):
        return (point1.price - point0.price) / (point1.id - point0.id)

    def compare_speed(self, current_speed, new_speed):
        if new_speed > current_speed:
            return True, False
        else:
            return False, True
