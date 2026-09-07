N = int(input())

for i in range(N):
    for j in range(2*(N-i), 2, -1):
        print(" ", end="")

    for j in range(2*i+1):
        print("* ", end="")
    print()