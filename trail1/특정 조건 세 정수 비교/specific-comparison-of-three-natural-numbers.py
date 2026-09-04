a, b, c = map(int, input().split())

if a == min(a, b, c):
    result1 = 1
else:
    result1 = 0

if a == b == c:
    result2 = 1
else:
    result2 = 0

print(result1, result2)