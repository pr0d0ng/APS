A = int(input())

for n in range(1, A+1):
    if (n % 2 == 0 and n % 4 != 0) or (n // 8) % 2 == 0 or n % 7 < 4:
        continue
    print(n, end=" ")