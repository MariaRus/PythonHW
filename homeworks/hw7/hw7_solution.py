import random


def check_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - bulls
    return bulls, cows


def generate_secret_number():
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))


def missing_statues(statues):
    if not statues:
        return 0

    min_size = min(statues)
    max_size = max(statues)
    total_statues = set(range(min_size, max_size + 1))
    current_statues = set(statues)
    missing = total_statues - current_statues
    return len(missing)


def infinity_loop(a, b):
    return (b - a) % 2 != 0
