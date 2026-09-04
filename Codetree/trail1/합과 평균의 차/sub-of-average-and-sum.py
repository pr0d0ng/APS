a, b, c = map(int, input().split())

sum = a + b + c
mean = int(sum / 3)
diff = sum - mean

print(sum)
print(mean)
print(diff)