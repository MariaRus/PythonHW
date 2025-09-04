def add_ing(s: str) -> str:
    words = s.split()
    return ' '.join([word + 'ing' for word in words])


def change_symbol(s: str) -> str:
    return s.replace('#', '/')


def change_order(s: str) -> str:
    words = s.split()
    return ' '.join(reversed(words))


def clean_string(s: str) -> str:
    return s.strip()


def to_capitalize(s: str) -> str:
    return s.capitalize()


def to_list(s: str) -> list:
    return s.split()


def formatting(array: list, s1: str, s2: str) -> str:
    return f"Hello, {' '.join(array)}! Welcome to {s1} {s2}"


def to_string(array: list) -> str:
    return ' '.join(array)


def insert_to_list(array: list, item: int | str, indx: int) -> list:
    array.insert(indx, item)
    return array


def delete_from_list(array: list, indx: int) -> list:
    if 0 <= indx < len(array):
        del array[indx]
    return array
