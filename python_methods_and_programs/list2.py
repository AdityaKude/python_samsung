list2 = [12, 3, 9, 5, 4, 5]
print(f'List2 = {list2}')
print(f'Sorted List2 = {sorted(list2)}') # sorts only the copy of list
print(f'List2 = {list2}')

print(list2.sort()) # prints None. Because sort() method returns Nothing
print(f'List2 = {list2}')

print(f'Index of 5 in List2 = {list2.index(5)}')
print(f'Index of 15 in List2 = {list2.index(15)}')