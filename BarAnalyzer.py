class BarAnalyzer:
    def __init__(self, data_walker):
        self.data_walker = data_walker

    def analyze_bar_based_on_index(self):
        if self.is_first_bar():
            self.data_walker.initialize_first_bar()
        elif self.is_second_bar():
            self.data_walker.analyze_second_bar()
        else:
            self.data_walker.analyze_general_bar()

    def is_first_bar(self):
        return self.data_walker.current_index == 0 and self.data_walker.current_trend is None

    def is_second_bar(self):
        return self.data_walker.current_index == 1 and self.data_walker.current_trend is None
