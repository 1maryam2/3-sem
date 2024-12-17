from lab_python_oop.shape_of_figure import Shape_of_figure
from lab_python_oop.color import Color_of_figure

class Rectangle(Shape_of_figure):#дописать про цвет
    shape = "Прямоугольник"
    @classmethod
    def get_shape(cls):
        return cls.shape
    def __init__(self, color, width, height):
        self.color = Color_of_figure()
        self.color.color_ = color
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def __repr__(self):
        return f'Название фигуры - {Rectangle.get_shape()}, цвет - {self.color.color_}, ширина - {self.width}, высота - {self.height}, площадь - {self.area()}'
