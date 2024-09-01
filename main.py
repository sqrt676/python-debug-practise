import math
from typing import List

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number.")
        self.result += value
    
    def subtract(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number.")
        self.result -= value
    
    def multiply(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number.")
        self.result *= value
    
    def divide(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number.")
        if value == 0:
            raise ValueError("Cannot divide by zero.")
        self.result /= value
    
    def sqrt(self):
        if self.result < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        self.result = math.sqrt(self.result)
    
    def clear(self):
        self.result = 0
    
    def __str__(self):
        return f"Current result: {self.result}"

def perform_operations(calculator: Calculator, operations: List[str], values: List[float]):
    for operation, value in zip(operations, values):
        if operation == 'add':
            calculator.add(value)
        elif operation == 'subtract':
            calculator.subtract(value)
        elif operation == 'multiply':
            calculator.multiply(value)
        elif operation == 'divide':
            calculator.divide(value)
        elif operation == 'sqrt':
            calculator.sqrt()
        elif operation == 'clear':
            calculator.clear()
        else:
            raise ValueError(f"Unknown operation: {operation}")

def main():
    calc = Calculator()
    operations = ['add', 'multiply', 'subtract', 'divide', 'sqrt', 'clear']
    values = [10, 5, 2, 0, 4, 1]

    try:
        perform_operations(calc, operations, values)
    except ValueError as e:
        print(f"Error: {e}")
    
    print(calc)

if __name__ == "__main__":
    main()
