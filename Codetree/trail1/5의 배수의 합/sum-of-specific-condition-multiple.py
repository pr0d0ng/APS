A, B = map(int, input().split())

sum = 0

if A <= B:
    for n in range(A, B+1):
        if n % 5 == 0:
            sum += n
elif A > B:
    for n in range(B, A+1):
        if n % 5 == 0:
            sum += n

print(sum)