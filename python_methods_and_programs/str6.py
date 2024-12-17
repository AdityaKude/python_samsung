s1 = 'gadag'
s2 = 'hospet'

print(f'Before Swap: \n S1 = {s1}, S2 = {s2}')
s1, s2 = s2, s1

# Implicitly a tuple is created and the RHS values is stored in it. And then the values from the tuple are copied one by one to the LHS variables.
print(f'After  Swap: \n S1 = {s1}, S2 = {s2}')