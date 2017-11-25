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

    def clone(self):
        return TwoDRectangularFigure(self.width, self.length)


class TwoDOvalFigure(object):
    def __init__(self, radius=1):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def clone(self):
        return TwoDOvalFigure(self.radius)


class FigureGraphics(object):
    def __init__(self, prototype):
        self.prototype = prototype

    def create_figure(self):
        return self.prototype.clone()


def main():
    graphics = FigureGraphics(TwoDOvalFigure(4))
    new_figure = graphics.create_figure()
    print("Oval figure area:", new_figure.calculate_area())
    graphics = FigureGraphics(TwoDRectangularFigure(4, 5))
    new_figure = graphics.create_figure()
    print("Rect figure area:", new_figure.calculate_area())

if __name__ == '__main__':
    main()
