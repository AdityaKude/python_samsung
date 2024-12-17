def partition_oranges(n, oranges):
    # The pivot is the last element
    pivot = oranges[n-1]
    
    k = 0
    # Loop through all the elements except the pivot
    for i in range(n-1):
        if oranges[i] <= pivot:
            # Swap oranges[i] and oranges[k] if the current orange is smaller than or equal to pivot
            oranges[i], oranges[k] = oranges[k], oranges[i]
            k += 1
    
    # Swap the pivot with the element at index k
    oranges[k], oranges[n-1] = oranges[n-1], oranges[k]
    
    # Return the partitioned list
    return oranges

# Input reading
n = int(input())  # The number of oranges
oranges = list(map(int, input().split()))  # The sizes of the oranges

# Get the result after partitioning
result = partition_oranges(n, oranges)

# Output the final arrangement of the oranges
print(' '.join(map(str, result)))



# Explanation of Code:
# Input:
# The number of oranges `n` is taken as input.
# The array of oranges (their diameters) is then input as a space-separated string,
# which is converted to a list of integers.

# Partition Function:
# The function partition_oranges performs the partitioning as described:
# - It uses a pivot (the last orange in the array).
# - It iterates through the list, and each time it finds an orange that is smaller than or equal to the pivot,
#   it swaps that orange to the left side of the list.
# - Finally, it places the pivot in its correct position, such that all the oranges smaller than or equal to the pivot
#   are on the left, and the oranges larger than the pivot are on the right.

# Output:
# After partitioning, the final array of orange sizes is printed, with the sizes of the oranges separated by spaces.

# Time Complexity:
# The partitioning process involves iterating over the array once, so the time complexity of this process is O(n),
# where `n` is the number of oranges.

# Example Walkthrough:
# Sample Input:
# 8
# 4 3 8 6 1 1 9 5
#
# Process:
# - The last orange (5) is selected as the pivot.
# - Partitioning will result in the following steps:
#   - Oranges smaller than or equal to 5 will be moved to the left.
#   - Oranges larger than 5 will be moved to the right.
#
# Step-by-Step Result:
# Initial: [4, 3, 8, 6, 1, 1, 9, 5]
# After partitioning: [4, 3, 1, 1, 5, 6, 9, 8]
# Final output: 4 3 1 1 5 6 9 8
