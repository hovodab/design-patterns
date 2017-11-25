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
        return copy.deepcopy(self)


class PassengerAirplane(AbstractAircraft):

    emulation = "Emulation of ==Passenger Airplane=="

    def clone(self):
        """
        Create wing for passenger airplane.

        :rtype: PassengerAirplaneWing
        :return: PassengerAirplaneWing object.
        """
        return copy.deepcopy(self)


class AircraftEmulator(object):
    """
    Emulator creator for aircraft of different types.
    """

    def __init__(self, prototype):
        self._airplane = prototype

    def create_new_aircraft(self):
        return self._airplane.clone()


def main():
    print("**************************************************")
    print()

    fighter = Fighter()
    passenger_airplane = PassengerAirplane()

    fighter_emulator1 = AircraftEmulator(fighter)
    fighter1 = fighter_emulator1.create_new_aircraft()
    fighter2 = fighter_emulator1.create_new_aircraft()

    passenger_emulator1 = AircraftEmulator(passenger_airplane)
    passenger_airplane1 = passenger_emulator1.create_new_aircraft()
    passenger_airplane2 = passenger_emulator1.create_new_aircraft()

    fighter1.show()
    fighter2.show()
    passenger_airplane1.show()
    passenger_airplane2.show()

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
