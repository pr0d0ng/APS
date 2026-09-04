T = 10

for tc in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    position_i = 0
    position_j = 0

    i = 99
    for j in range(100):
        if arr[i][j] == 2:
            position_i = i
            position_j = j
            break

    prev_i = 0
    prev_j = 0

    while not position_i == 0:
        for di, dj in [[0,1], [0,-1], [-1,0]]:
            ni, nj = position_i+di, position_j+dj
            if 0 <= ni < 100 and 0 <= nj < 100:
                if (arr[ni][nj] == 1) and (ni,nj) != (prev_i,prev_j):
                    prev_i = position_i
                    prev_j = position_j
                    position_i = ni
                    position_j = nj

    print(f"#{tc} {position_j}")