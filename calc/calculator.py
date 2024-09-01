import math
from typing import List, Union, Dict

from calc.base import Calculator

class BasicCalculator(Calculator):
    '''A basic calculator that implements the Calculator interface'''

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class ComplexCalculator(BasicCalculator):
    '''A class for complex calculations'''
    
    def __init__(self):
        super().__init__()
        self.operation: Union[List, Dict] = []

    def max_in_list(self, listToOperate: List[int]) -> int:
        """Return the maximum element of an integer list

        Args:
            listToOperate (List[int]): A list of integers

        Returns:
            int: The maximum integer in the list
        """
        if not listToOperate:
            raise ValueError("The list is empty")
        return max(listToOperate)
