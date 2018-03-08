def is_isogram(string):
    usedLetters = []
    allowedChars = [' ', '-']
    for char in string.lower():
        if char not in allowedChars and char in usedLetters:
            return False
        usedLetters.append(char)
    return True
