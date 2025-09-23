def remove_previous_symbol(text):
    if not text:
        return ""

    result = []
    for char in text:
        if char == '#':
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)
