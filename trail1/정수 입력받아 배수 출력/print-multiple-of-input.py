N = int(input())

for i in range(N, 5 * N + 1):
    if i % N == 0:
        print(i, end=" ")