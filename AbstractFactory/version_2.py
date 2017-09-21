#!/usr/bin/python3
# Author: Geghetsik Dabaghyan

from abc import abstractmethod, ABCMeta
import math


class AbstractFigure(metaclass=ABCMeta):
    @abstractmethod
    def calculateArea(self):
        pass


class RectangularFigure(AbstractFigure):
    def __init__(self, width=1, length=1):
        self.width = width
        self.length = length

    def calculateArea(self):
        return self.width * self.length


class OvalFigure(AbstractFigure):
    def __init__(self, radius=1):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius ** 2


class AbstractFigureFactory(metaclass=ABCMeta):
    @abstractmethod
    def createFigure(self):
        pass


class RectangularFigureFactory(AbstractFigureFactory):
    def createFigure(self):
        return RectangularFigure()


class OvalFigureFactory(AbstractFigureFactory):
    def createFigure(self):
        return OvalFigure()


def main():
    my_figure1 = RectangularFigureFactory().createFigure()
    print('Rectangle area:', my_figure1.calculateArea())
    my_figure2 = OvalFigureFactory().createFigure()
    print('Oval area:', my_figure2.calculateArea())


if __name__ == '__main__':
    main()
