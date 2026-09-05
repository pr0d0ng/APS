a, b, c = map(int, input().split())

flag = "NO"

for n in range(a, b+1):
    if n % c == 0:
        flag = "YES"
    
print(flag)