numbers = []
count = 0

for i in range(6):
    num = float(input())
    numbers.append(num)

for number in numbers:
    if number >= 0:
        count += 1

print(f"{count} valores positivos")
average = sum(num for num in numbers if num >= 0) / count # this is new
print(f"{average:.1f}")