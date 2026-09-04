N = int(input())

sum = 0

for n in range(1, N):
    if N % n == 0:
        sum += n
        
if sum == N:
    print('P')
else:
    print('N')
