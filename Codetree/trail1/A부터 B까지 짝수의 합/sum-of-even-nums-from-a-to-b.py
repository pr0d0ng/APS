A, B = map(int, input().split())

even_sum = 0

for n in range(A, B+1):
    if n % 2 == 0:
        even_sum += n

print(even_sum)