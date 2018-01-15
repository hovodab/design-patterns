#!/usr/bin/python3
# Author: Hovhannes Dabaghyan


class Observer(object):
    """
    Observer interface.
    """

    def changed_event(self, observable):
        """
        Get event about observable subject change.

        :type observable: Observable
        :param observable: Observable object.

        :rtype: void
        :return: void
        """
        print("Observer object is notified about observable change: {}".format(observable.get_state()))


class Observable(object):
    """
    Observable interface.
    """

    def __init__(self):
        self._state = None
        self._observers = list()

    def register_observer(self, observer):
        """
        Register observer for observable object.

        :type observer: Observer
        :param observer: Observer object which should be registered in order to get notifications.

        :rtype: void
        :return: void
        """
        self._observers.append(observer)

    def remove_observer(self, observer):
        """
        Remove observer from list of observer objects.

        :type observer: Observer
        :param observer: Observer object which should be removed in order to not get notifications.

        :rtype: void
        :return: void
        """
        self._observers.remove(observer)

    def notify(self):
        """
        Notify all observers about change.

        :rtype: void
        :return: void
        """
        for observer in self._observers:
            observer.changed_event(self)

    def set_state(self, state):
        """
        Set state of the observable object.

        :type state: str
        :param state: Some state.

        :rtype: void
        :return: void
        """
        self._state = state
        self.notify()

    def get_state(self):
        """
        Get current state of the observable object.

        :rtype: str|NoneType
        :return: Current state of object.
        """
        return self._state


def main():
    print("**************************************************")
    print()

    observable = Observable()
    observer1 = Observer()
    observer2 = Observer()
    observable.register_observer(observer1)
    observable.register_observer(observer2)
    observable.set_state("Some change...")
    observable.remove_observer(observer1)
    observable.set_state("Some other change...")


    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
