#!/usr/bin/python3
# Author: Hovhannes Dabaghyan


class SingletoneMeta(type):
    """
    Singletone metaclass.
    """
    _exemplars = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._exemplars:
            cls._exemplars[cls] = super().__call__(*args, **kwargs)
        return cls._exemplars[cls]


class Singletone(object, metaclass=SingletoneMeta):
    """
    Singletone class example.
    """
    def __init__(self):
        self.prop = 15


def main():
    print("**************************************************")
    print()
    s1 = Singletone()
    s1.prop = 77
    print("First object prop: {}".format(s1.prop))
    print("Creating second object...")
    s2 = Singletone()
    print("Second object prop: {}".format(s2.prop))
    print("Changing second object prop to 1...")
    s2.prop = 1
    print("First object prop: {}".format(s1.prop))

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
