T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_num = list(map(int, input().split()))

    arr = [0] * (N+1)
    for i in range(len(charge_num)):
        arr[charge_num[i]] = 1

    charge_sum = 0
    position = 0
    while position < N-K:
        stop_list = []
        stop = position + 1
        while stop <= position+K:
            if arr[stop]:
                stop_list.append(stop)
                charge_sum += 1
                stop += 1
            else:
                stop += 1

        if len(stop_list) > 1:
            charge_sum -= (len(stop_list) - 1)

        if stop_list:
            position = max(stop_list)
        else:
            charge_sum = 0
            break

    print(f"#{tc} {charge_sum}")