N = int(input())  # Number of test cases
inside = 0
outside = 0

for _ in range(N):
    x = int(input())
    if 10 <= x <= 20:
        inside += 1
    else:
        outside += 1

print(f"{inside} in")
print(f"{outside} out")