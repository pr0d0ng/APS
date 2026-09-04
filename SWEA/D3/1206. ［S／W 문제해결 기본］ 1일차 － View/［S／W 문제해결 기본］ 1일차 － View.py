T = 10

for tc in range(1, T+1):
    building_num = int(input())
    building_height = list(map(int, input().split()))

    view = 0
    for b in range(building_num - 4):
        if building_height[b+2] > max(building_height[b], building_height[b+1], building_height[b+3], building_height[b+4]):
            view += building_height[b + 2] - max(building_height[b], building_height[b + 1], building_height[b + 3], building_height[b + 4])

    print(f"#{tc} {view}")
