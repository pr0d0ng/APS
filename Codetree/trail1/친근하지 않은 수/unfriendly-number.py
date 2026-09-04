N = int(input())

cnt = 0

for n in range(1, N+1):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        cnt += 1

print(cnt)