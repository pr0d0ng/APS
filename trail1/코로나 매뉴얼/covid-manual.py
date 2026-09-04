A = B = C = D = 0

for _ in range(3):
    c, t = input().split()
    t = int(t)

    if c == "Y":
        if t >= 37:
            A += 1
        else:
            C += 1
    else:
        if t >= 37:
            B += 1
        else:
            D += 1

if A >= 2:
    print("E")
else:
    print("N")