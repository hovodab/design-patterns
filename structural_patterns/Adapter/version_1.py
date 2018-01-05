#!/usr/bin/python3
# Author: Hovhannes Dabaghyan


class Sensor(object):
    """
    Singleton metaclass.
    """

    def calculate(self, outcome_adc, max_force, adc_max):
        """
        Calculate force in Newtons.

        :type outcome_adc: int
        :param outcome_adc: Outcome from sensor in ADC format.

        :type max_force: int
        :param max_force: Maximum force that sensor is able to measure.

        :type adc_max: int
        :param adc_max: ADC value of the maximum force load of th sensor.

        :rtype: float
        :return: Calculated force in Newtons.
        """
        return outcome_adc * max_force / float(adc_max)


class SimplifierSensorAdapter(object):
    """
    Very simple adapter-simplifier for calculate method.
    Uses class parameters as method arguments.
    """

    MAX_FORCE = 1000
    ADC_MAX = 5000

    def __init__(self):
        self.sensor = Sensor()

    def calculate(self, outcome_adc):
        """
        Calculate force in Newtons for specific sensor.

        :type outcome_adc: int
        :param outcome_adc: Outcome from sensor in ADC format.

        :rtype: int
        :return: Calculated force in Newtons.
        """
        return self.sensor.calculate(outcome_adc, self.MAX_FORCE, self.ADC_MAX)


def main():
    print("**************************************************")
    print()
    s = SimplifierSensorAdapter()
    print("Load/power on sensor: {} N".format(s.calculate(1000)))
    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
