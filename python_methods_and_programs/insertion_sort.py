import sys

def insertion_sort(numbers):
    for i in range (1, len(numbers)):
        element = numbers[i]
        j = i - 1
        while j >= 0 and element < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = element
        print(numbers)

size = int(sys.argv[1])
numbers = []

print(f'Enter {size} numbers of the array')
for i in range(size):
    numbers.append(int(input()))

print('Input Array is: \n ', numbers)
insertion_sort(numbers)
print('Sorted Array is: \n ', numbers)