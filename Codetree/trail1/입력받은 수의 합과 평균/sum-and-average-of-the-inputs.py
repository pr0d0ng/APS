N = int(input())

sum = 0
cnt = 0

for _ in range(N):
    n = int(input())
    sum += n
    cnt += 1

print(f"{sum} {sum/cnt:.1f}")