while True:
    n = int(input())
    if n == 0:
        break   
    else:
        if n % 2 != 0:
            n += 1  # make sure it starts from even

        even_numbers = []
        
        for i in range(n, n + 10, 2):  # now picks 5 even numbers
            even_numbers.append(i)

        print(sum(even_numbers))