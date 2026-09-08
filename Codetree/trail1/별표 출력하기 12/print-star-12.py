N = int(input())

total_rows = 1 if N == 1 else 2 * (N // 2)

for r in range(total_rows):
    row = []
    for c in range(N):
        if r == 0 or (c % 2 == 1 and c >= r):
            row.append("*")
        else:
            row.append(" ")

    print(" ".join(row).rstrip())