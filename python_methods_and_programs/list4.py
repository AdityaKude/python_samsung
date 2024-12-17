arr1 = [11, 7, 5, 3, 2, 0]

arr2 = arr1 # Shallow copy (only reference is copied)
arr2[1] = 25
arr3 = list(arr1) # Deep Copy
arr3[1] = 35
arr4 = arr1.copy() # Deep Copy
arr4[1] = 45

print('Arr1=',arr1)
print('Arr2=',arr2)
print('Arr3=',arr3)
print('Arr1=',arr1)
print('Arr4=',arr4)
print('Arr1=',arr1)
arr1[2] = 50
print('Arr1=',arr1)
print('Arr2=',arr2)
arr3[3] = 100
print('Arr1=',arr1)
print('Arr3=',arr3)
arr3[2] = 200
print('Arr1=',arr1)
print('Arr4=',arr3)