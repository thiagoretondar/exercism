def is_pangram(sentence):
    all_alphabet_letters = set([chr(char) for char in range(ord('a'), ord('z'))])
    all_letters_in_sentence = set(sentence.lower())
    return all_alphabet_letters.issubset(all_letters_in_sentence)