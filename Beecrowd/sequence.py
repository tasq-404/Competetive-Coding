while True:
    a, b = map(int, input().split())
    if a <= 0 or b <= 0:
        break
    total = 0
    for i in range(min(a, b), max(a, b) + 1):
        total += i
        print(i, end=' ')
    print(f'Sum={total}')