#!/usr/bin/python3
# Author: Hovhannes Dabaghyan

import copy
from abc import ABCMeta, abstractmethod
from utils.helpers import FancyObject


class AbstractAircraft(FancyObject, metaclass=ABCMeta):
    """
    Aircraft creator. Just interfaces.
    """

    emulation = "Emulation of Aircraft."

    @abstractmethod
    def clone(self):
        """
        Create wing for aircraft.
        """
        pass

    def show(self):
        self.fancy_print(self.emulation)


class Fighter(AbstractAircraft):
    """
    Fighter aircraft.
    """
    emulation = "Emulation of >>Fighter>> aircraft."

    def clone(self):
        """
        Create wing for fighter.

        :rtype: FighterWing
        :return: FighterWing object.
        """
        return Fighter()


class PassengerAirplane(AbstractAircraft):

    emulation = "Emulation of ==Passenger Airplane=="

    def clone(self):
        """
        Create wing for passenger airplane.

        :rtype: PassengerAirplaneWing
        :return: PassengerAirplaneWing object.
        """
        return PassengerAirplane()


class AircraftEmulator(object):
    """
    Emulator for aircraft of different types.
    """

    def __init__(self, prototype):
        self._airplane = copy.deepcopy(prototype)

    def emulate(self):
        self._airplane.show()


def main():
    print("**************************************************")
    print()

    fighter = Fighter()
    passenger_airplane = PassengerAirplane()

    aircraft_emulator1 = AircraftEmulator(fighter)
    aircraft_emulator2 = AircraftEmulator(passenger_airplane)

    aircraft_emulator1.emulate()
    aircraft_emulator2.emulate()

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
