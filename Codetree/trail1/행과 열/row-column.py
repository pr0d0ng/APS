A, B = map(int, input().split())

arr = [[0] * B for _ in range(A)]

for i in range(A):
    for j in range(B):
        arr[i][j] = (i+1)*(j+1)

for i in range(A):
    print(' '.join(map(str, arr[i])))