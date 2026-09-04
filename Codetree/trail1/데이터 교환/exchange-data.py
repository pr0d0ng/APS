a, b, c = 5, 6, 7

temp_a = a
temp_b = b
temp_c = c

b = a
c = temp_b
a = temp_c

print(a)
print(b)
print(c)