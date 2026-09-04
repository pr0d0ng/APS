N = int(input())

cnt = 1
i = 1

while N > 1:
    i += 1
    cnt += 1
    N //= i

print(cnt)