A, B = map(int, input().split())

product = 1

for n in range(1, B+1):
    if n % A == 0:
        product *= n

print(product)