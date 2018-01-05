#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
import time


class SolarPanels(object):
    """
    Class representing component that we have.
    """

    def deploy(self):
        print("Solar panels: Solar panels deployed...")
        print()


class RocketStage(object):
    """
    Rocket stage.
    """
    def disconnect(self, timeout):
        time.sleep(timeout)
        print("RocketStage: Rocket stage disconnected...")
        print()


class Engine(object):
    """
    Rocket engine.
    """
    @staticmethod
    def start(slogan):
        print("Engine: Engine started...")
        print("Engine: " + slogan)
        print()


class Satellite(object):
    """
    Facade for all parts.
    """

    def __init__(self):
        self._engine = Engine()
        self._rocket_stage = RocketStage()
        self._solar_panels = SolarPanels()

    def deploy(self):
        self._engine.start("To infinity and beyond.")
        self._rocket_stage.disconnect(1)
        self._solar_panels.deploy()
        print("Satellite is on orbit...")


def main():
    print("**************************************************")
    print()
    Satellite().deploy()
    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
