T = 10

for tc in range(1, T+1):
    test_case = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    sum_list = []
    for i in range(100):
        s_row = 0
        for j in range(100):
            s_row += arr[i][j]
        sum_list.append(s_row)

    for j in range(100):
        s_col = 0
        for i in range(100):
            s_col += arr[i][j]
        sum_list.append(s_col)

    s_diag = 0
    for i in range(100):
        s_diag += arr[i][i]
        sum_list.append(s_diag)

    s_antidiag = 0
    for i in range(100):
        s_antidiag = arr[i][99-i]
        sum_list.append(s_antidiag)

    result = max(sum_list)

    print(f"#{tc} {result}")