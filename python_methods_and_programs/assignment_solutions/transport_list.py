from collections import Counter

def find_missing_numbers(arr, brr):
    # Create counters for both lists
    arr_count = Counter(arr)
    brr_count = Counter(brr)
    
    # Find missing numbers by comparing the counts
    missing_numbers = []
    
    for num in arr_count:
        if arr_count[num] > brr_count[num]:
            missing_numbers.append(num)
    
    # Return the sorted list of missing numbers
    return sorted(missing_numbers)

# Reading input
n = int(input())  # Size of the first list (arr)
arr = list(map(int, input().split()))  # Elements of the first list (arr)
m = int(input())  # Size of the second list (brr)
brr = list(map(int, input().split()))  # Elements of the second list (brr)

# Get the missing numbers
result = find_missing_numbers(arr, brr)

# Output the result
print(" ".join(map(str, result)))



# Create counters for both lists
# arr_count = Counter(arr)  # Count occurrences of each number in the original list (arr)
# brr_count = Counter(brr)  # Count occurrences of each number in the current list (brr)

# Find missing numbers by comparing the counts
# missing_numbers = []  # Initialize an empty list to store missing numbers

# Loop through each number in the original list (arr)
# for num in arr_count:
#     if arr_count[num] > brr_count[num]:  # If the count of num is greater in arr than in brr
#         missing_numbers.append(num)  # Add the missing number to the list

# Return the sorted list of missing numbers
# return sorted(missing_numbers)  # Sort and return the missing numbers in ascending order

# Reading input
# n = int(input())  # Read the size of the first list (arr)
# arr = list(map(int, input().split()))  # Read the n space-separated integers for the original list (arr)
# m = int(input())  # Read the size of the second list (brr)
# brr = list(map(int, input().split()))  # Read the m space-separated integers for the current list (brr)

# Get the missing numbers
# result = find_missing_numbers(arr, brr)  # Call the function to find missing numbers

# Output the result
# print(" ".join(map(str, result)))  # Print the missing numbers as space-separated integers
# The original list arr = [1, 2, 3, 4, 5]
# The current list brr = [3, 1, 2, 4, 5, 5]

# From the comparison:
# The number 5 appears twice in brr but only once in arr,
# indicating that one occurrence of 5 is missing from arr.

# So, the output is 5.
