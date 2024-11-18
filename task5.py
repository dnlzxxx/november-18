with open('part1.txt', 'r') as first, open('part2.txt','r') as second, open('full_next.txt', 'w') as final:
    for line in first:
        final.write(line)

    for line in second:
        final.write(line)