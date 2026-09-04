N = int(input())

for s in range(N, 101):
    if s >= 90:
        print("A", end=" ")
    elif s >= 80:
        print("B", end=" ")
    elif s >= 70:
        print("C", end=" ")
    elif s >= 60:
        print("D", end=" ")
    elif s < 60:
        print("F", end=" ")    