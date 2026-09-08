N = int(input())

for i in range(N):
    if i % 2:
        print("* " * (i+1))
    else:
        print("* " * 1)