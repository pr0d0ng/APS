N = int(input())

for i in range(N):
    print("  " * (N-1-i), end="")
    print("@ " * (1+i))

for i in range(N):
    print("@ " * (N-1-i))