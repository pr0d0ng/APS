N = int(input())

for i in range(N):
    if i % 2:
        print("* " * (N- (i-1)//2))
    else:
        print("* " * (1 + i//2))

for i in range(N-1, -1, -1):
    if i % 2:
        print("* " * (N- (i-1)//2))
    else:
        print("* " * (1 + i//2))
