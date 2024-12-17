import abc

class Shape_of_figure(abc.ABC):
    @abc.abstractmethod
    def area(self): pass    #площадь фигуры
