numbers = []
for _ in range(5):
    num = float(input())
    numbers.append(num)


even_count = sum(1 for number in numbers if number % 2 == 0)
print(f"{even_count} valores pares")