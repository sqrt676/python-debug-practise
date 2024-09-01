''' Main block to execute a module by creating object'''
# Here I am trying to make an entry script

from calc.calculator import BasicCalculator
from calc.calculator import ComplexCalculator

def main():
    '''main block of entry script'''
    calculator_object = BasicCalculator()
    complex_object = ComplexCalculator()
    result = calculator_object.add(5,10)
    result2 = complex_object.max_in_list([1,2,3])
    print(f"The result of the addition is: {result} and list Op is {result2}")

if __name__ == '__main__':
    main()
    