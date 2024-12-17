# Default Arguments
def find_remainder(num1 = 25, num2 = 10):
    return num1 % num2

print('10 % 20 = ',find_remainder(10, 20))
print('10 % 10 = ',find_remainder(10))
print('25 % 10 = ',find_remainder())
print('15 % 35 = ',find_remainder(num1 = 15, num2 = 35))
print('20 % 10 = ',find_remainder(num2 = 10, num1 = 20)) # Named Args