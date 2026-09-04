N = int(input())

for n in range(1, N+1):
    if (n % 3 == 0) or ('3' in str(n)) or ('6' in str(n)) or ('9' in str(n)):
        print(0, end=" ")
    else:
        print(n, end=" ")