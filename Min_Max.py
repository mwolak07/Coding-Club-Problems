arr = [0, 7, 2, 5, 2]

maxval = 0

for element in arr:
    if element > maxval:
        maxval = element

minval = maxval

for element in arr:
    if element < minval:
        minval = element

print(maxval)
print(minval)