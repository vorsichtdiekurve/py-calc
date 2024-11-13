"""
Module containing the Calculator class
"""

class Calculator:
    """
    Calculator class

    Implements basic mathematical operations (+, -, * /) on floating point numbers.
    """

    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self):
        """ Function performing the addition operation

            Returns:
                float: Sum of two numbers
        """
        return self.__op1 + self.__op2

    def subtract(self):
        """ Function performing the subtraction operation

            Returns:
                float: Difference of two numbers
        """
        return self.__op1 - self.__op2

    def multiply(self):
        """ Function performing the multiplication operation

            Returns:
                float: Product of two numbers
        """
        return self.__op1 * self.__op2

    def divide(self):
        """ Function performing the division operation

            Returns:
                float: Quotient of two numbers
        """
        return self.__op1 / self.__op2
