# (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
def verify(isbn):
    isbn_numbers = isbn.replace('-', '')
    isbn_sum = 0
    if len(isbn_numbers) < 10:
        return False

    for char_index in range(0, 10):
        if isbn_numbers[char_index] == 'X':
            isbn_sum = isbn_sum + (10 * (10 - char_index))
        elif isbn_numbers[char_index].isdigit():
            isbn_sum = isbn_sum + int(isbn_numbers[char_index]) * (10 - char_index)
        print(char_index, (10 - char_index), isbn_sum)
    return isbn_sum % 11 == 0
