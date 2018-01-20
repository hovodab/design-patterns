#!/usr/bin/python3
# Author: Hovhannes Dabaghyan


from abc import ABCMeta, abstractmethod


class Visitor(object, metaclass=ABCMeta):
    """
    Visitor interface.
    """

    @abstractmethod
    def visit_a(self, element):
        """
        Visit `A` type elements. Perform operation on `A` type element.

        :type element: Element
        :param element: Element on which operation should be performed.

        :rtype: void
        :return: void
        """
        raise NotImplementedError()

    @abstractmethod
    def visit_b(self, element):
        """
        Visit `B` type elements. Perform operation on `B` type element.

        :type element: Element
        :param element: Element on which operation should be performed.

        :rtype: void
        :return: void
        """
        raise NotImplementedError()


class PrintVisitor(Visitor):
    """
    Prints information about elements.
    """

    def visit_a(self, element):
        """
        Visit `A` type elements. Perform operation on `A` type element.

        :type element: Element
        :param element: Element on which operation should be performed.

        :rtype: void
        :return: void
        """
        print("A specific implementation of print operation.")

    def visit_b(self, element):
        """
        Visit `B` type elements. Perform operation on `B` type element.

        :type element: Element
        :param element: Element on which operation should be performed.

        :rtype: void
        :return: void
        """
        print("B specific implementation of print operation.")


class Element(object, metaclass=ABCMeta):
    """
    Rocket carrier with solid fuel.
    """

    @abstractmethod
    def accept(self, visitor):
        """
        Write code in C.

        :rtype: void
        :return: void
        """
        raise NotImplementedError()


class ElementA(Element):
    """
    Concrete node of the system.
    """

    def accept(self, visitor):
        """
        Accept visitor which will perform operation. Call operation for self class `A`.

        :type visitor: Visitor
        :param visitor: Visitor which should perform operations.

        :rtype: void
        :return: void
        """
        visitor.visit_a(self)


class ElementB(Element):
    """
    Concrete node of the system.
    """

    def accept(self, visitor):
        """
        Accept visitor which will perform operation. Call operation for self class `B`.

        :type visitor: Visitor
        :param visitor: Visitor which should perform operations.

        :rtype: void
        :return: void
        """
        visitor.visit_b(self)


def main():
    print("**************************************************")
    print()

    elements = [ElementA(), ElementB()]
    visitor = PrintVisitor()
    for element in elements:
        element.accept(visitor)

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
