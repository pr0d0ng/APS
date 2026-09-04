A, N = map(int, input().split())

result = A + N

for _ in range(N):
    print(result)
    result += N    