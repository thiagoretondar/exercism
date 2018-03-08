def reverse(input=''):
    if (not len(input)):
        return input
    else:
        return reverse(input[1:]) + input[:1]
