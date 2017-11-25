#!/usr/bin/python3
# Author: Geghetsik Dabaghyan

from abc import abstractmethod, ABCMeta
import math


class TwoDRectangularFigure(object):
    def __init__(self, width=1, length=1):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length


class TwoDOvalFigure(object):
    def __init__(self, radius=1):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class ThreeDRectangularFigure(object):
    def __init__(self, width=1, length=1, height=1):
        self.width = width
        self.length = length
        self.height = height

    def calculate_volume(self):
        return self.width * self.length * self.height


class ThreeDOvalFigure(object):
    def __init__(self, radius=1):
        self.radius = radius

    def calculate_volume(self):
        return (4 * math.pi * self.radius ** 3) / 3


class AbstractFigureBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.oval = None
        self.rect = None

    def create_oval(self, data):
        pass

    def create_rect(self, data):
        pass

    def get_figure(self):
        return self.oval, self.rect


class TwoDFigureBuilder(AbstractFigureBuilder):
    def create_oval(self, data):
        self.oval = TwoDOvalFigure(data[0])

    def create_rect(self, data):
        self.rect = TwoDRectangularFigure(*data)


class ThreeDFigureBuilder(AbstractFigureBuilder):
    def create_oval(self, data):
        self.oval = ThreeDOvalFigure(data[0])

    def create_rect(self, data):
        self.rect = ThreeDRectangularFigure(*data)


class FigureDirector(object):
    def __init__(self, builder):
        self.builder = builder

    def create_figure(self, *data):
        self.builder.create_oval(data)
        self.builder.create_rect(data)


def main():
    two_d_builder = TwoDFigureBuilder()
    director = FigureDirector(two_d_builder)
    director.create_figure(2, 3)
    circle, rect = two_d_builder.get_figure()
    print("Circle Area: ", circle.calculate_area())
    print("Rect Area: ", rect.calculate_area())

    three_d_builder = ThreeDFigureBuilder()
    director = FigureDirector(three_d_builder)
    director.create_figure(2, 3, 4)
    sphere, cube = three_d_builder.get_figure()
    print("Sphere Volume: ", sphere.calculate_volume())
    print("Cube Volume: ", cube.calculate_volume())


if __name__ == '__main__':
    main()
