import sys

def bubble_sort(numbers):
    for i in range (len(numbers)-1):
        sorted = True
        for j in range(len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                sorted = False
        if sorted:
            return

size = int(sys.argv[1])
numbers = []

print(f'Enter {size} numbers of the array')
for i in range(size):
    numbers.append(int(input()))

print('Input Array is: \n ', numbers)
bubble_sort(numbers)
print('Sorted Array is: \n ', numbers)