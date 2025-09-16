import random


def check_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - bulls
    return bulls, cows


def generate_secret_number():
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))
