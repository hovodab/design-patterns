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


class AbstractAircraft(metaclass=ABCMeta):
    """
    Aircraft creator. Just interfaces.
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


class Fighter(AbstractAircraft):
    """
    Fighter aircraft.
    """

    def create_wing(self):
        """
        Create wing for fighter.

        :rtype: FighterWing
        :return: FighterWing object.
        """
        return FighterWing()

    def create_tail(self):
        """
        Create tail for fighter.

        :rtype: FighterTail
        :return: FighterTail object.
        """
        return FighterTail()

    def create_wheels(self):
        """
        Create wheels for fighter.

        :rtype: FighterWheels
        :return: FighterWheels object.
        """
        return FighterWheels()


class PassengerAirplane(AbstractAircraft):

    def create_wing(self):
        """
        Create wing for passenger airplane.

        :rtype: PassengerAirplaneWing
        :return: PassengerAirplaneWing object.
        """
        return PassengerAirplaneWing()

    def create_tail(self):
        """
        Create wing for passenger airplane.

        :rtype: PassengerAirplaneTail
        :return: PassengerAirplaneTail object.
        """
        return PassengerAirplaneTail()

    def create_wheels(self):
        """
        Create wing for passenger airplane.

        :rtype: PassengerAirplaneWheels
        :return: PassengerAirplaneWheels object.
        """
        return PassengerAirplaneWheels()


def main():
    print("**************************************************")
    print()

    aircraft1 = Fighter()
    aircraft2 = PassengerAirplane()
    print(aircraft1.create_wing().show())
    print(aircraft2.create_wing().show())

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
