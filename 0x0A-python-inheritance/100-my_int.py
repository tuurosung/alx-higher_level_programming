#!/usr/bin/python3


class MyInt(int):
    """Inverts operators"""

    def __eq__(self, value):
        """Redirect == operand with != """
        return self.real != value

    def __ne__(self, value):
        """Redirect != operand with =="""
        return self.real == value
