import sys

def binary_search(numbers, search_key):
    low = 0
    high = len(numbers) - 1
    while(low <= high):
        mid = (low + high) // 2
        if numbers[mid] == search_key:
            return mid
        elif search_key < numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

size = int(sys.argv[1])
numbers = []

print(f'Enter {size} numbers of the array')
for i in range(size):
    numbers.append(int(input()))

numbers.sort()
search_key = int(input('Enter the element to be searched: '))

index = binary_search(numbers, search_key)
print('The inpur array is: \n', numbers)
if index == -1:
    print(f'The number {search_key} was not found')
else:
    print(f'The number {search_key} was found at index {index}')
