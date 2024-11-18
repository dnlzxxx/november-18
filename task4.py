with open('story.txt', 'r') as f, open('new_story.txt', 'w') as another:
    for line in f:
        another_one = line.replace("Python", "Java")
        another.write(another_one)