N = int(input())

arr = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        arr[i][j] = 2*j + 11 + 2*i
    
for row in arr:
    print(' '.join(map(str, row)))