import sys

def partitionArray(array):
    pivot = array[-1]
    j = 0
    for i in range(len(array)-1):
        if array[i] < pivot:
            array[j], array[i] = array[i], array[j]
            j += 1
    array[j], array[-1] = array[-1], array[j] # bring the pivot element to its final position


size = int(sys.argv[1])
print(f'Enter {size} numbers of the Array')
numbers = []
for i in range(size):
    numbers.append(int(input()))

print('Input Array is \n', numbers)
partitionArray(numbers) #call by reference
print('Partitioned Array is \n', numbers)