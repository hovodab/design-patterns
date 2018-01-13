#!/usr/bin/python3
# Author: Hovhannes Dabaghyan

import time
from abc import ABCMeta, abstractmethod


class Command(object, metaclass=ABCMeta):
    """
    Interface for all commands.
    """

    @abstractmethod
    def execute(self):
        """
        Entry-point for all commands.

        :rtype: void
        :return: void
        """
        raise NotImplementedError()


class DeploySolarPanelsCommand(Command):
    """
    Command for deploying solar panels.
    """

    def __init__(self, solar_panels):
        self._solar_panels = solar_panels

    def execute(self):
        """
        Invoke deployment.

        :rtype: void
        :return: void
        """
        self._solar_panels.deploy()


class DisconnectRocketStageCommand(Command):
    """
    Command for rocket stage disconnection.
    """

    def __init__(self, rocket_stage):
        self._rocket_stage = rocket_stage

    def execute(self):
        """
        Invoke stage disconnect.

        :rtype: void
        :return: void
        """
        self._rocket_stage.disconnect(1)


class StartEngineCommand(Command):
    """
    Command for engine start.
    """

    def __init__(self, engine):
        self._engine = engine

    def execute(self):
        """
        Invoke engine start.

        :rtype: void
        :return: void
        """
        self._engine.start("Per aspera ad astra.")


class SolarPanels(object):
    """
    Receiver class representing rocket solar panels.

        ###
         ###
      \___###_____
    < )___________< ~~..
     /     ###
            ###
             ###
    """

    def deploy(self):
        print("Solar panels: Solar panels deployed...")
        print()


class RocketStage(object):
    """
    Receiver class representing rocket stage.
    """
    def disconnect(self, timeout):
        time.sleep(timeout)
        print("RocketStage: Rocket stage disconnected...")
        print()


class Engine(object):
    """
    Receiver class representing rocket engine.
    """
    @staticmethod
    def start(slogan):
        print("Engine: Engine started...")
        print("Engine: " + slogan)
        print()


class Satellite(object):
    """
    Invoker class sending commands to all parts.
    """

    def __init__(self):
        self._engine = Engine()
        self._rocket_stage = RocketStage()
        self._solar_panels = SolarPanels()

    def deploy(self):
        """
        Deploy satellite to orbit.

        :rtype: void
        :return: void
        """
        StartEngineCommand(self._engine).execute()
        DisconnectRocketStageCommand(self._rocket_stage).execute()
        DeploySolarPanelsCommand(self._solar_panels).execute()


def main():
    print("**************************************************")
    print()

    satellite = Satellite()
    satellite.deploy()

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
