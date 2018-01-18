#!/usr/bin/python3
# Author: Hovhannes Dabaghyan


from abc import ABCMeta, abstractmethod


class Programmer(object, metaclass=ABCMeta):
    """
    Programmer interface.
    """

    def wake_up(self):
        """
        Wake up wake up, grab a brush and put a little makeup.

        :rtype: void
        :return: void
        """
        print(str(self) + " wakes up.")

    def go_to_work(self):
        """
        Go to work

        :rtype: void
        :return: void
        """
        print(str(self) + " goes to work.")

    @abstractmethod
    def write_code(self):
        """
        This is what should do a programmer at work.

        :rtype: void
        :return: void
        """
        raise NotImplementedError()

    def go_to_sleep(self):
        """
        It's enough for that day. Get a little rest.

        :rtype: void
        :return: void
        """
        print(str(self) + " goes to sleep.")

    def live_usual_day(self):
        """
        Live a usual programmer day.

        :rtype: void
        :return: void
        """
        self.wake_up()
        self.go_to_work()
        self.write_code()
        self.go_to_sleep()

    def __str__(self):
        return "Programmer"


class CProgrammer(Programmer):
    """
    Rocket carrier with solid fuel.
    """

    def write_code(self):
        """
        Write code in C.

        :rtype: void
        :return: void
        """
        print(str(self) + " writes code in C.")

    def __str__(self):
        return "C programmer"


class PythonProgrammer(Programmer):

    def write_code(self):
        """
        Write code for fun.

        :rtype: void
        :return: void
        """
        print(str(self) + " writes code in beautiful Python.")

    def __str__(self):
        return "Python programmer"


def main():
    print("**************************************************")
    print()

    c_programmer = CProgrammer()
    python_programmer = PythonProgrammer()
    print()
    print("Day of a C programmer:")
    c_programmer.live_usual_day()
    print()
    print("Day of a Python programmer:")
    python_programmer.live_usual_day()

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
