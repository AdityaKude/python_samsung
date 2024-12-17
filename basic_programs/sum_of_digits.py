import sys

input_number = int(sys.argv[1])
print(f'User given number is {input_number}')

digits = [int(digit) for digit in sys.argv[1]]
print(f'Sum of the digits of {input_number} is {sum(digits)}')