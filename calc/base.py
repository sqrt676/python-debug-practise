from abc import ABC, abstractmethod

class Calculator(ABC):
    '''Base class for all calculators'''

    def __init__(self):
        pass

    @abstractmethod
    def add(self, a: float, b: float) -> float:
        '''Perform addition'''
        pass

    @abstractmethod
    def subtract(self, a: float, b: float) -> float:
        '''Perform subtraction'''
        pass

    @abstractmethod
    def multiply(self, a: float, b: float) -> float:
        '''Perform multiplication'''
        pass

    @abstractmethod
    def divide(self, a: float, b: float) -> float:
        '''Perform division'''
        pass
