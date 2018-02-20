#!/usr/bin/python3
# Author: Geghetsik Dabaghyan


class SingletonWindowsManager(object):
    __instance__ = None
    __windows_number = 0

    def create_window(self):
        SingletonWindowsManager.__windows_number += 1

    def get_windows_number(self):
        return SingletonWindowsManager.__windows_number

    def __call__(self, *args, **kwargs):
        if SingletonWindowsManager.__instance__ is None:
            SingletonWindowsManager.__instance__ = SingletonWindowsManager()
        return SingletonWindowsManager.__instance__


def main():
    manager1 = SingletonWindowsManager()
    print("Windows number1: ", manager1.get_windows_number())
    print("Create window manager 1")
    manager1.create_window()
    print("Create window manager 1")
    manager1.create_window()
    print("Windows number1: ", manager1.get_windows_number())

    manager2 = SingletonWindowsManager()
    print("Windows number2: ", manager2.get_windows_number())
    print("Create window manager 2")
    manager2.create_window()
    print("Windows number1: ", manager1.get_windows_number())
    print("Windows number2: ", manager2.get_windows_number())


if __name__ == '__main__':
    main()
