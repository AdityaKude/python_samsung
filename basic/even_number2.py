# Check if the user given number is Even or not.

print('Enter a number to check if it is Even or not')
input_number = int(input())
#print(type(input_number))

if input_number % 2 == 0:
    print(input_number, ' is an Even number')
else:
    print(f'{input_number} is not an Even number')
