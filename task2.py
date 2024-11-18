with open("data.txt","r") as f, open("even_numbers.txt", "w") as another:
    for line in f:
        numbers = line.split()
        for num in numbers:
            if int(num) % 2 == 0:
                another.write(str(num) + " ")