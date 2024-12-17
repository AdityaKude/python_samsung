def my_Function():
   yield "Hello"
   yield 51
   yield "Good Bye"
   return 5.5

x = my_Function()
print('Type of X = ', type(x))
#print('Length of X = ', len(x))

for value in x:
    print('Type of Value =', type(value), '  Value =', value)

#Can read Values from a generator only once
print('X = ', list(x))
