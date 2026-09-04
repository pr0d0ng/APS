N = int(input())

if N >= 3000:
    print("book")
elif 1000 <= N < 3000:
    print("mask")
elif 500 <= N < 1000:
    print("pen")
else:
    print("no")