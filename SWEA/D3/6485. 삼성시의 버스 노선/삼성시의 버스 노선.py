T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 5001
    route = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(route[i][0], route[i][1]+1):
            bus_stop[j] += 1

    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))

    result = []
    for i in C:
        result.append(bus_stop[i])

    print(f"#{tc} {' '.join(map(str, result))}")