N = int(input())

product = 1

for n in range(1, 11):
    product *= n
    if product >= N:
        print(n)
        break