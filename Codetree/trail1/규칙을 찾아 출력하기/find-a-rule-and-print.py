N = int(input())

for r in range(N):
    if r == 0 or r == N - 1:
        print(" ".join(["*"] * N))
    else:
        row = ["*"] * r + [" "] * (N - 1 - r) + ["*"]
        print(" ".join(row))