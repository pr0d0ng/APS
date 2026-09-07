N = int(input())

for n in range(N, 0, -1):
    for _ in range(n):
        print("*" * n, end=" ")
    print()