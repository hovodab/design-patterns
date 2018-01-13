#!/usr/bin/python3
# Author: Hovhannes Dabaghyan

from abc import ABCMeta, abstractmethod


class Context(object):
    """
    Context.
    """
    pass


class BasicExpression(object, metaclass=ABCMeta):
    """
    Interface of expression.
    """

    @abstractmethod
    def interpret(self, context):
        raise NotImplementedError()


class TerminalExpression(BasicExpression):
    """
    Terminal expression representation.
    """
    def interpret(self, context):
        print("Terminal expression.")


class NonTerminalExpression(BasicExpression):
    """
    Non terminal expression representation.
    """
    def interpret(self, context):
        print("Non Terminal expression")


def main():
    print("**************************************************")
    print()

    context = Context()
    expressions = list()
    expressions.append(TerminalExpression())
    expressions.append(NonTerminalExpression())
    expressions.append(TerminalExpression())
    expressions.append(TerminalExpression())
    expressions.append(NonTerminalExpression())
    for expression in expressions:
        expression.interpret(context)

    print()
    print("**************************************************")

if __name__ == '__main__':
    main()
