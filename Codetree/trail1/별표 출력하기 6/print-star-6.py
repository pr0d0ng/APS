N = int(input())

for i in range(2*N-1, 0, -2):
    print(" " * (2*N-1-i), end="")
    print("* " * i)

for i in range(3, 2*N, 2):
    print(" " * (2*N-1-i), end="")
    print("* " * i)