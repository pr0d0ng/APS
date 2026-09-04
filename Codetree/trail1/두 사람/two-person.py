a1, s1 = input().split()
a2, s2 = input().split()

if (int(a1) >= 19 and s1 == "M") or (int(a2) >= 19 and s2 == "M"):
    print(1)
else:
    print(0)