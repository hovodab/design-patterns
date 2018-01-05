#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
from abc import ABCMeta, abstractmethod


class ComponentInterface(object, metaclass=ABCMeta):
    """
    Interface for components and for their decorators.
    """

    @abstractmethod
    def do_something(self):
        raise NotImplementedError()


class Component(ComponentInterface):
    """
    Class representing component that we have.
    """

    def do_something(self):
        print("This is some operation.")


class Wrapper(ComponentInterface):
    """
    Wraps other components.
    """

    def __init__(self, component):
        self._component = component

    def do_something(self):
        print("_______________________")
        self._component.do_something()
        print("-----------------------")


def main():
    print("**************************************************")
    print()
    component = Component()
    wrapper = Wrapper(component)
    print("Without wrapping...")
    component.do_something()
    print()
    print("With wrapping...")
    wrapper.do_something()
    print()
    print("With double wrapping...")
    Wrapper(wrapper).do_something()
    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
