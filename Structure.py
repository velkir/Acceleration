from AbstractStructure import AbstractStructure


class Structure(AbstractStructure):
    def __init__(self):
        super().__init__(structure=None)

    def add_trend(self, trend):
        self.structure.append(trend)

    @property
    def length(self):
        return len(self.structure)

    def get_current_trend_layer(self):
        pass
