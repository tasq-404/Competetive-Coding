numbers = []
for _ in range(6):
    numbers.append(float(input()))

# count the positive
positive = 0
for num in numbers:
    if num > 0:
        positive += 1

print(f"{positive} valores positivos")