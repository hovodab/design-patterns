#!/usr/bin/python3
# Author: Hovhannes Dabaghyan

from weakref import proxy
from abc import ABCMeta, abstractmethod


class Mediator(object, metaclass=ABCMeta):
    """
    Mediator interface.
    """
    EVENT_VIOLATION_ON = 0
    EVENT_VIOLATION_OFF = 1

    @abstractmethod
    def event(self):
        raise NotImplementedError()


class Colleague(object, metaclass=ABCMeta):
    """
    Components used in mediator.
    """

    def __init__(self, mediator):
        # Proxy is used to except cyclic references.
        self._mediator = proxy(mediator)

    @abstractmethod
    def trigger_event(self):
        raise NotImplementedError()


class ForceSensor(Colleague):
    """
    Force sensor representing class.
    """

    def trigger_event(self, event):
        self._mediator.event(event)


class RedLamp(Colleague):
    """
    Class representing red lamp.
    """

    def trigger_event(self):
        pass

    def light_on(self):
        print("Light turned on...")

    def light_off(self):
        print("Light turned off...")


class NoiseDynamic(Colleague):
    """
    class representing noise device/dynamic.
    """

    def trigger_event(self):
        pass

    def noise_on(self):
        print("Noise is on...")

    def noise_off(self):
        print("Noise is off...")


class AlarmingDirector(Mediator):
    """
    Custom mediator for handling sensors and alarming functionality.
    """

    def __init__(self):
        self.force_sensor = ForceSensor(self)
        self.red_lamp = RedLamp(self)
        self.noise = NoiseDynamic(self)

    def event(self, event):
        if event == self.EVENT_VIOLATION_ON:
            self.red_lamp.light_on()
            self.noise.noise_on()
        elif event == self.EVENT_VIOLATION_OFF:
            self.red_lamp.light_off()
            self.noise.noise_off()


def main():
    print("**************************************************")
    print()

    alarm_director = AlarmingDirector()
    alarm_director.force_sensor.trigger_event(Mediator.EVENT_VIOLATION_ON)
    print('==================================================')
    alarm_director.force_sensor.trigger_event(Mediator.EVENT_VIOLATION_OFF)

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
