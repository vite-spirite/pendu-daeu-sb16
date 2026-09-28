from random import random

def selection_mot():
    file = open('dictionnaire.txt', mode='r', encoding='utf8')

    content = file.read()
    file.close()

    lines = content.splitlines()
    selected_idx = int(random() * (len(lines) + 1))
    return lines[selected_idx].split(';')[0]

print(selection_mot())