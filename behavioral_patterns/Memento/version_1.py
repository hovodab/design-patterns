#!/usr/bin/python3
# Author: Hovhannes Dabaghyan

from weakref import proxy
from abc import ABCMeta, abstractmethod


class Memento(object):
    """
    Memento object.
    """

    def __init__(self, position):
        self._position = position

    def get_position(self):
        """
        Get saved state.

        :rtype: int
        :return: Saved position.
        """
        return self._position

    def __str__(self):
        return "Current position: {}".format(self._position)


class BrakeActuator(object):
    """
    Represents brake actuator. Is Originator.
     ___________
    |           =  Retracted position.
    |__________|
     ___________
    |           ====  Extracted position.
    |__________|
    """
    MIN_POSITION = 0
    MAX_POSITION = 800

    def __init__(self):
        # Brake is retracted.
        self._position = 0

    def drive_steps(self, steps):
        """
        Drive brake actuator with given steps.

        :type steps: int
        :param steps: How much drive the brake. Could be negative in that case will be retracted.

        :rtype: void
        :return: void
        """
        self._position += steps
        if self._position > 800:
            self._position = 800
        if self._position < 0:
            self._position = 0

    def get_state(self):
        """
        Get current state of the brake actuator.

        :rtype: Memento
        :return: Return Memento object holding current state.
        """
        return Memento(self._position)

    def set_state(self, memento):
        """
        Set to given state.

        :type memento: Memento
        :param memento: Set state to given Memento object.

        :rtype: void
        :return: void
        """
        self._position = memento.get_position()


def main():
    print("**************************************************")
    print()

    # This part takes responsibilities of Caretaker.
    brake_actuator = BrakeActuator()
    brake_actuator.drive_steps(10)
    brake_actuator.drive_steps(-20)
    state_1 = brake_actuator.get_state()
    brake_actuator.drive_steps(8000)
    print(brake_actuator.get_state())
    brake_actuator.set_state(state_1)
    print(brake_actuator.get_state())


    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
