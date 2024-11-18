kol_chars = 0
kol_words = 0
kol_strok = 0

with open("text.txt", "r") as f:
    for line in f:
        kol_strok += 1
        words = line.split()
        kol_words += len(words)
        kol_chars += len(line)

print("Количество строк:", kol_strok)
print("Количество слов:", kol_words)
print("Количество символов:", kol_chars)