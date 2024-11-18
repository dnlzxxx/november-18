with open('input.txt', "r") as f, open('output.txt', 'w') as another:
    for line in f:
        upper_line = line.upper()
        another.write(upper_line)