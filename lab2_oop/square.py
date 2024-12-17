from lab_python_oop.color import Color_of_figure
from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    shape = "Квадрат"
    Rectangle.get_shape()
    def __init__(self, color, side):
        self.color = Color_of_figure()
        self.color.color_ = color
        self.side = side
    def area(self):
        return pow(self.side, 2)
    def __repr__(self):
        return f'Название фигуры - {Square.get_shape()}, цвет - {self.color.color_}, длина одной стороны - {self.side}, площадь - {self.area()}'