# Two ways to create an empty list:
list1 = []
list2 = list()

list1.append(10) # Add an element at the rear end of the list
list1.append(20)

list1.insert(1, 25)
print(list1)
print('Popped element is',list1.pop())
# pop() method removes element from rear and returns it.

list1.extend([10, 19])
# Extend the list1 with the elements of the given list
print(list1) # [10, 25, 10, 19]

list2 = list(list1)
# we can initialize a list into another while creation (copy of the list)
del list2[0]
print(f'List1 = {list1} \nList2 = {list2}')
list1.clear() # empties the list. But the list remains
print(f'List1 = {list1}')

del list1
# It deletes the list altogether. Now list1 doesn't exist at all.
print(list1) # Causes NameError

print('Sum of List2 elements = ', sum(list2))
print('Length of List2 = ', len(list2))
print('Type of List2 = ', type(list2))
