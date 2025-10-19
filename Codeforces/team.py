T = int(input())
solution = 0
for _ in range(T):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:  # sum >= 2 means at least two people solved it
        solution += 1
print(solution)
