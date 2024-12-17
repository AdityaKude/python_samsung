import sys

def partitionArray(array, low, high):
    pivot = array[high]
    j = low
    for i in range(low, high):
        if array[i] < pivot:
            array[j], array[i] = array[i], array[j]
            j += 1
    array[j], array[high] = array[high], array[j] # bring the pivot element to its final position
    return j

def quick_sort(numbers, low, high):
    if low < high:
        pivot_index = partitionArray(numbers, low, high)
        print(numbers)
        quick_sort(numbers, low, pivot_index-1)
        quick_sort(numbers, pivot_index+1, high)


size = int(sys.argv[1])
print(f'Enter {size} numbers of the Array')
numbers = []
for i in range(size):
    numbers.append(int(input()))

print('Input Array is \n', numbers)
quick_sort(numbers, 0, len(numbers)-1) #call by reference
print('Sorted Array is \n', numbers)