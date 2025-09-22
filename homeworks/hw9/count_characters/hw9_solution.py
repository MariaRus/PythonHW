def count_char(text):
    if not text:
        return ""

    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(text[i - 1])
            if count > 1:
                result.append(str(count))
            count = 1

    # Добавляем последний символ и его количество
    result.append(text[-1])
    if count > 1:
        result.append(str(count))

    return ''.join(result)
