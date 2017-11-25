#!/usr/bin/python3
# Author: Hovhannes Dabaghyan

from abc import ABCMeta, abstractmethod
from utils.helpers import FancyObject


class AbstractWing(FancyObject, metaclass=ABCMeta):
    """
    Wing functionality interface. Just show.
    """
    @abstractmethod
    def show(self):
        pass

    def __repr__(self):
        return self.__class__.__name__


class AbstractTail(FancyObject, metaclass=ABCMeta):
    """
    Tail functionality interface. Just show.
    """
    @abstractmethod
    def show(self):
        pass

    def __repr__(self):
        return self.__class__.__name__


class AbstractWheels(FancyObject, metaclass=ABCMeta):
    """
    Wheels functionality interface. Just show.
    """
    @abstractmethod
    def show(self):
        pass

    def __repr__(self):
        return self.__class__.__name__


class FighterWing(AbstractWing):
    """
    Wing of fighter. With implemented functionality for fighter.
    """
    def show(self):
        self.fancy_print("Fighter Wing ^")


class FighterTail(AbstractTail):
    """
    Tail of fighter. With implemented functionality for fighter.
    """
    def show(self):
        self.fancy_print("Fighter Tail I_I")


class FighterWheels(AbstractWheels):
    """
    Wheels of fighter. With implemented functionality for fighter.
    """
    def show(self):
        self.fancy_print("Fighter Wheels oo o")


class PassengerAirplaneWing(AbstractWing):
    """
    Wing of passenger airplane. With implemented functionality for passenger airplane.
    """
    def show(self):
        self.fancy_print("Passenger Airplanes Wing /\\")


class PassengerAirplaneTail(AbstractTail):
    """
    Tail of passenger airplane. With implemented functionality for passenger airplane.
    """
    def show(self):
        self.fancy_print("Passenger Airplanes Tail T")


class PassengerAirplaneWheels(AbstractWheels):
    """
    Wheels of passenger airplane. With implemented functionality for passenger airplane.
    """
    def show(self):
        self.fancy_print("Passenger Airplanes Wheels OO OO O")


class AbstractAircraftBuilder(metaclass=ABCMeta):
    """
    Aircraft builder. Just interfaces.
    """
    @abstractmethod
    def create_wing(self):
        """
        Create wing for aircraft.
        """
        pass

    @abstractmethod
    def create_tail(self):
        """
        Create tail for aircraft.
        """
        pass

    @abstractmethod
    def create_wheels(self):
        """
        Create wheels for aircraft.
        """
        pass

    @abstractmethod
    def get_aircraft(self):
        """
        Get built aircraft.
        """
        pass


class FighterBuilder(AbstractAircraftBuilder):
    """
    Fighter aircraft builder.
    """
    def __init__(self):
        self.aircraft = dict()

    def create_wing(self):
        """
        Create wing for fighter.

        :rtype: FighterWing
        :return: FighterWing object.
        """
        self.aircraft['wing'] = FighterWing()

    def create_tail(self):
        """
        Create tail for fighter.

        :rtype: FighterTail
        :return: FighterTail object.
        """
        self.aircraft['tail'] = FighterTail()

    def create_wheels(self):
        """
        Create wheels for fighter.

        :rtype: FighterWheels
        :return: FighterWheels object.
        """
        self.aircraft['wheels'] = FighterWheels()

    def get_aircraft(self):
        return self.aircraft


class PassengerAirplaneBuilder(AbstractAircraftBuilder):
    """
    Passenger airplane builder.
    """

    def __init__(self):
        self.aircraft = dict()

    def create_wing(self):
        """
        Create wing for passenger airplane.

        :rtype: PassengerAirplaneWing
        :return: PassengerAirplaneWing object.
        """
        self.aircraft['wing'] = PassengerAirplaneWing()

    def create_tail(self):
        """
        Create wing for passenger airplane.

        :rtype: PassengerAirplaneTail
        :return: PassengerAirplaneTail object.
        """
        self.aircraft['tail'] = PassengerAirplaneTail()

    def create_wheels(self):
        """
        Create wing for passenger airplane.

        :rtype: PassengerAirplaneWheels
        :return: PassengerAirplaneWheels object.
        """
        self.aircraft['wheels'] = PassengerAirplaneWheels()

    def get_aircraft(self):
        return self.aircraft


class AircraftBuilderDirector(object):
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.create_wing()
        self.builder.create_tail()
        self.builder.create_wheels()
        return self.builder.get_aircraft()


def main():
    print("**************************************************")
    print()

    aircraft1 = AircraftBuilderDirector(FighterBuilder()).construct()
    aircraft2 = AircraftBuilderDirector(PassengerAirplaneBuilder()).construct()
    print(aircraft1)
    print(aircraft2)

    print()
    print("Aircraft 1:")
    aircraft1['wing'].show()
    aircraft1['tail'].show()
    aircraft1['wheels'].show()

    print()
    print("Aircraft 2:")
    aircraft2['wing'].show()
    aircraft2['tail'].show()
    aircraft2['wheels'].show()

    print()
    print("**************************************************")


if __name__ == '__main__':
    main()
