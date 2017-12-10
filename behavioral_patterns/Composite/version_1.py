#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
from abc import ABCMeta, abstractmethod


class SubWeb(object, metaclass=ABCMeta):
    """
    Abstraction for all nodes.
    """

    @abstractmethod
    def do_something(self):
        raise NotImplementedError()


class Element(SubWeb):
    """
    Class representing elementary node.
    """

    def do_something(self, margin):
        print(margin + "Final element.")


class Web(SubWeb):
    """
    Represents combined elements.
    """

    def __init__(self):
        self._elements = []

    def add_element(self, sub_web):
        self._elements.append(sub_web)

    def do_something(self, margin=""):
        print(margin + "Web Element containing...")
        for element in self._elements:
            element.do_something(margin + "  ")


def main():
    print("**************************************************")
    print()
    web = Web()
    element1 = Element()
    element2 = Element()
    element3 = Web()
    element4 = Element()
    web.add_element(element1)
    web.add_element(element2)
    element3.add_element(element4)
    web.add_element(element3)
    web.do_something()
    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
