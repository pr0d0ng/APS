A, B = map(int, input().split())

product = 1

for n in range(A, B+1):
    product *= n

print(product)