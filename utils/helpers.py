#!/usr/bin/python3

import math


class FancyObject(object):
    """
    Fancy helper class.
    """
    @staticmethod
    def fancy_print(message):
        """
        Print message in fancy way.

        :type message: str
        :param message: Message to be printed in fancy-mancy way.

        :rtype: void
        :return: void
        """
        pre_post = 50
        spaces_length_left = math.ceil((pre_post - 2 - len(message)) / 2)
        spaces_length_right = spaces_length_left - (2 * spaces_length_left + 2 + len(message) - pre_post)
        print('=' * pre_post)
        print("!" + " " * spaces_length_left + message + " " * spaces_length_right + "!")
        print('=' * pre_post)