#!/usr/bin/python3
# Author: Hovhannes Dabaghyan


from weakref import proxy
from abc import ABCMeta, abstractmethod


class RocketCarrierStrategy(object, metaclass=ABCMeta):
    """
    Unit system state interface.
    """

    @abstractmethod
    def execute(self):
        """
        Burn something and deliver rocket to the destination.

        :rtype: void
        :return: void
        """
        raise NotImplementedError()


class SolidFuelRocketCarrier(RocketCarrierStrategy):
    """
    Rocket carrier with solid fuel.
    """

    def execute(self):
        """
        Burn solid fuel and deliver rocket to the destination.

        :rtype: void
        :return: void
        """
        print("Burning solid fuel...")


class LiquidFuelRocketCarrier(RocketCarrierStrategy):
    """
    Rocket carrier with liquid fuel.
    """

    def execute(self):
        """
        Burn liquid fuel and deliver rocket to the destination.

        :rtype: void
        :return: void
        """
        print("Burning liquid(not water of course) fuel...")


class Rocket(object):
    """
    Rocket that should fly to Alpheratz.
    """

    def __init__(self):
        self._carrier = LiquidFuelRocketCarrier()

    def to_infinity_and_beyond(self):
        """
        Deliver rocket to Andromeda alpha star: Alpheratz.

        :rtype: void
        :return: void
        """
        self._carrier.execute()

    def set_carrier(self, carrier):
        """
        Set carrier of the rocket.

        :type carrier: RocketCarrierStrategy
        :param carrier: Rocket carrier strategy object.

        :rtype: void
        :return: void
        """
        self._carrier = carrier


def main():
    print("**************************************************")
    print()

    rocket = Rocket()
    rocket.set_carrier(SolidFuelRocketCarrier())
    rocket.to_infinity_and_beyond()
    rocket.set_carrier(LiquidFuelRocketCarrier())
    rocket.to_infinity_and_beyond()

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
