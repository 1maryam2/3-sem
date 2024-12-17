class Color_of_figure:
    def __init__(self):
        self.color = None
    @property
    def color_(self):
        return self.color
    @color_.setter
    def color_(self, new_color):
        self.color = new_color
