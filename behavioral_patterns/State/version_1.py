#!/usr/bin/python3
# Author: Hovhannes Dabaghyan


from weakref import proxy
from abc import ABCMeta, abstractmethod


class SystemState(object, metaclass=ABCMeta):
    """
    Unit system state interface.
    """

    def __init__(self, machine):
        self._machine = machine

    @abstractmethod
    def get_size(self):
        """
        Get size.

        :rtype: float
        :return: Size of the machine.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_mass(self):
        """
        Get mass.

        :rtype: float
        :return: Mass of the machine.
        """
        raise NotImplementedError()


class CSystemState(SystemState):
    """
    C unit system state.
    """

    def get_size(self):
        """
        Get size in meters.

        :rtype: float
        :return: Size of the machine.
        """
        return self._machine.size

    def get_mass(self):
        """
        Get mass in kilograms.

        :rtype: float
        :return: Mass of the machine.
        """
        return self._machine.mass


class ISystemState(SystemState):
    """
    Imperial unit system state.
    """

    def get_size(self):
        """
        Get size in yards.

        :rtype: float
        :return: Size of the machine.
        """
        return self._machine.size * 0.9144

    def get_mass(self):
        """
        Get mass in pounds.

        :rtype: float
        :return: Mass of the machine.
        """
        return self._machine.mass * 0.45359237


class Machine(object):
    """
    Machine which has mass and size.
    """

    def __init__(self, size, mass):
        self.size = size
        self.mass = mass
        self._state = ISystemState(proxy(self))

    def get_size(self):
        """
        Get size in configured system.

        :rtype: float
        :return: Size of the machine.
        """
        return self._state.get_size()

    def get_mass(self):
        """
        Get mass in configured system.

        :rtype: float
        :return: Mass of the machine.
        """
        return self._state.get_mass()

    def set_state(self, state):
        self._state = state(proxy(self))


def main():
    print("**************************************************")
    print()

    machine = Machine(7, 2000)
    machine.set_state(CSystemState)
    print("Machine size and wight in system `C`", machine.get_size(), machine.get_mass())
    machine.set_state(ISystemState)
    print("Machine size and wight in system `Imperial`", machine.get_size(), machine.get_mass())

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
