
T = 10

for tc in range(1, T+1):
    dump_limit = int(input())
    height = list(map(int, input().split()))

    for dump in range(dump_limit):
        max_index = height.index(max(height))
        min_index = height.index(min(height))
        height[max_index] -= 1
        height[min_index] += 1

        if max(height) - min(height) <= 1:
            break

    print(f"#{tc} {max(height)-min(height)}")