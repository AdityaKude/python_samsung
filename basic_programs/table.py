# cline1.py
import sys

input_number = int(sys.argv[1])

for i in range(1, input_number+1):
    for j in range(1, input_number+1):
        if i == j or j == input_number - i + 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
