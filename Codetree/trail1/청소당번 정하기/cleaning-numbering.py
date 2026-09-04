clsroom = 0
hallway = 0
toilet = 0

n = int(input())

for d in range(1, n+1):
    if d % 12 == 0:
        toilet += 1
    elif d % 3 == 0:
        hallway += 1
    elif d % 2 == 0:
        clsroom += 1

print(clsroom, hallway, toilet)