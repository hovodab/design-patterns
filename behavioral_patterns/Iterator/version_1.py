#!/usr/bin/python3
# Author: Hovhannes Dabaghyan


class Iterator(object):
    """
    Basic iterator class running over object fields.
    """

    def __init__(self, obj, fields):
        self.object = obj
        self.fields = fields

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > len(self.fields) - 1:
            raise StopIteration()
        value = getattr(self.object, self.fields[self.index])
        self.index += 1
        return value


class Sample(Iterator):
    """
    Custom class which properties could be run over.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__(self, ['a', 'b'])


def main():
    print("**************************************************")
    print()

    iterator = Sample(12, 58)
    for i in iterator:
        print(i)

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
