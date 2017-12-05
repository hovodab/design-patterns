#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
from abc import ABCMeta, abstractmethod


class Sensor(object, metaclass=ABCMeta):
    """
    Sensor abstraction.
    """

    @abstractmethod
    def form_value(self):
        raise NotImplementedError()


class ForceSensor(Sensor):
    """
    Force sensor specific class.
    """
    FORCE_SENSOR_STAFF = "FORCE SENSOR"

    def form_value(self):
        return self.FORCE_SENSOR_STAFF


class OtherSensor(Sensor):
    """
    Some other sensor specific class.
    """
    OTHER_SERNSOR_STAFF = "OTHER SENSOR"

    def form_value(self):
        return self.OTHER_SERNSOR_STAFF


class Filter(object, metaclass=ABCMeta):
    """
    Signal filter abstraction.
    """

    def __init__(self, sensor):
        self._sensor = sensor

    @abstractmethod
    def calculate(self):
        raise NotImplementedError()


class LowPassFilter(Filter):
    """
    Low pass filter.
    """
    SOME_LOW_PASS_STAFF = "LOW PASS FILTERED"

    def calculate(self):
        return self._sensor.form_value() + ' ' + self.SOME_LOW_PASS_STAFF


class AverageFilter(Filter):
    """
    Average signal filter.
    """
    SOME_AVERAGE_STAFF = "AVERAGE FILTERED"

    def calculate(self):
        return self._sensor.form_value() + ' ' + self.SOME_AVERAGE_STAFF


def main():
    print("**************************************************")
    print()
    print(LowPassFilter(ForceSensor()).calculate())
    print(AverageFilter(ForceSensor()).calculate())
    print(LowPassFilter(OtherSensor()).calculate())
    print(AverageFilter(OtherSensor()).calculate())
    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
