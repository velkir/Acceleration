class StatusManager:
    def __init__(self, data_walker):
        self.data_walker = data_walker

    def check_and_change_status(self):
        if self.data_walker.current_trend:
            confirmed_layers = self.data_walker.config.Layers.confirmed_layers
            if self.data_walker.current_trend.layer >= confirmed_layers:
                self.data_walker.current_trend.status = 1
                self.change_parent_status(self.data_walker.current_trend.parent_trend)

    def change_parent_status(self, trend):
        if trend is not None:
            trend.status = 1
            self.change_parent_status(trend.parent_trend)
