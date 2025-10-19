T = int(input())

#total = 0

for _ in range(T):
    total = 0
    x, y = map(int, input().split())
    for i in range(min(x, y) + 1, max(x, y)):
        if i % 2 != 0:
            total += i
    print(total)