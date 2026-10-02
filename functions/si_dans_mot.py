def si_dans_mot(char, word):
    for i in word:
        if char == i:
            return True

    return False