T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    bin_sum = []
    for i in range(len(num) - M + 1):
        bin_sum.append(sum((num[i:i+M])))

    result = max(bin_sum) - min(bin_sum)

    print(f"#{tc} {result}")