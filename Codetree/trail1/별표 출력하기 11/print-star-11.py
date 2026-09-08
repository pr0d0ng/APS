N = int(input())

for i in range(2*N+1):
    if i % 2:
        print("*   " * (N+1))
    else:
        print("* " * (2*N+1))