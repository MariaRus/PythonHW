def motor_time(n):
    hours = (n // 60) % 24
    minutes = n % 60
    time_str = f"{hours:02d}{minutes:02d}"
    return sum(int(digit) for digit in time_str)


def level_up(experience, threshold, reward):
    total_experience = experience + reward
    return total_experience >= threshold


def time_converter(time_24):
    hours, minutes = map(int, time_24.split(':'))

    if hours == 0:
        return f"12:{minutes:02d} a.m."
    elif hours == 12:
        return f"12:{minutes:02d} p.m."
    elif hours > 12:
        return f"{hours - 12}:{minutes:02d} p.m."
    else:
        return f"{hours}:{minutes:02d} a.m."
