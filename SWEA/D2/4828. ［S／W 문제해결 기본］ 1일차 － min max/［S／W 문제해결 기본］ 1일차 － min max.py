T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 양의 정수의 개수
    numbers = list(map(int, input().split()))

    # 최댓값, 최솟값
    max_value = 0
    for i in range(N):
        if max_value < numbers[i]:
            max_value = numbers[i] # 최댓값 갱신

    min_value = 1000000
    for i in range(N):
        if min_value > numbers[i]:
            min_value = numbers[i]

    result = max_value - min_value

    print(f"#{tc} {result}")