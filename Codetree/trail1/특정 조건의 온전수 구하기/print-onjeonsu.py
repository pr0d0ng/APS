N = int(input())

for n in range(1, N+1):
    if n % 2 != 0 and str(n)[-1] != '5' and (n % 3 != 0 or n % 9 == 0):
        print(n, end=" ")