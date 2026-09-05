sum = 0
cnt = 0

for _ in range(101):
    a = int(input())
    
    if not 20 <= a < 30:
        break
    
    sum += a
    cnt += 1

print(f"{sum/cnt:.2f}")