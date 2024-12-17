import math
from lab_python_oop.shape_of_figure import Shape_of_figure
from lab_python_oop.color import Color_of_figure

class Circle(Shape_of_figure):
    shape = "Круг"
    @staticmethod
    def get_shape():
        return Circle.shape
    def __init__(self, color, radius):
        self.color = Color_of_figure()
        self.color.color_ = color
        self.radius = radius
    def area(self):
        return pow(self.radius, 2)*math.pi
    def __repr__(self):
        return f'Название фигуры - {Circle.get_shape()}, цвет - {self.color.color_}, радиус - {self.radius}, площадь - {self.area()}'
