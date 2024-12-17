str1 = '     hubballi  dharwad \t '

print(str1.strip().capitalize(), '***')
print('Count of a =',str1.count('a'))
print('Count of a =',str1.count('a', 12))
print('Count of a =',str1.count('a', 11, 15))

print('Index of h =', str1.find('h'))
print('Index of h =', str1.find('h', 10))
print('Index of h =', str1.find('h', 17, 20))

print('Index of h =', str1.index('h'))
print('Index of h =', str1.index('h', 10))
print('Index of h =', str1.index('h', 17, 20))