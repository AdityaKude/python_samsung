s1 = "123"
s2 = "²"
s3 = "½"
s4 = "IV"

print(s1.isdigit(), s1.isnumeric(), s1.isdecimal()) # True True True
print(s2.isdigit(), s2.isnumeric(), s2.isdecimal()) # True True False
print(s3.isdigit(), s3.isnumeric(), s3.isdecimal()) # False True False
print(s4.isdigit(), s4.isnumeric(), s4.isdecimal()) # False True False