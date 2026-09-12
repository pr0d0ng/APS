n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
position = n * 10

arr = [0] * (n * 10 * 2 + 1)

for i in range(n):
    if dir[i] == 'L':
        for j in range(position-x[i],position):
            arr[j] += 1
        position -= x[i]
    elif dir[i] == 'R':
        for j in range(position,position+x[i]):
            arr[j] += 1
        position += x[i]

cnt = 0

for n in arr:
    if n >= 2:
        cnt += 1

print(cnt)