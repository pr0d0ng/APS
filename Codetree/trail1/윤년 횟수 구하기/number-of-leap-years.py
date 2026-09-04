N = int(input())

ly = 0

for y in range(1, N+1):
    if y % 4 == 0:
        ly += 1
        if y % 100 == 0 and y % 400 != 0:
            ly -= 1

print(ly)