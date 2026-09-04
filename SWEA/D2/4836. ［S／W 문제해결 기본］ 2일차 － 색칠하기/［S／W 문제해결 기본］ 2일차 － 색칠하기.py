T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * 10 for _ in range(10)]

    color_arr = []
    for k in range(N):
        color_arr.append(list(map(int, input().split())))

        for i in range(color_arr[k][0], color_arr[k][2]+1):
            for j in range(color_arr[k][1], color_arr[k][3]+1):
                arr[i][j] += 1

    purple_count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                purple_count += 1

    print(f"#{tc} {purple_count}")