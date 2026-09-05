A, B = map(int, input().split())

flag = 0

for n in range(A, B+1):
    if 1920 % n == 0 and 2880 % n == 0:
        flag = 1

print(flag)