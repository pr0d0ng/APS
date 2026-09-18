N = int(input())

for k in range(1, N+1):
    for i in range(N, 0, -1):
        print(i*k, end=" ")
    print()