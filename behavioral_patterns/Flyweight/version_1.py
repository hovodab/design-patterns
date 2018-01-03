#!/usr/bin/python3
# Author: Hovhannes Dabaghyan

from abc import ABCMeta, abstractmethod


class Flyweight(metaclass=ABCMeta):
    """
    Flyweight base.
    """

    def __init__(self):
        self.intrinsic_state = False

    @abstractmethod
    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    """
    Concrete flyweight class implementing operation with extrinsic state.
    """

    def operation(self, extrinsic_state):
        pass


class FlyweightFactory(object):
    """
    Factory for flyweights.
    """

    def __init__(self):
        self._instances = {}

    def get_instance(self, key):
        if key not in self._instances:
            self._instances[key] = ConcreteFlyweight()
        return self._instances[key]


def main():
    print("**************************************************")
    print()

    factory = FlyweightFactory()

    factory.get_instance("first")
    factory.get_instance("second")

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
