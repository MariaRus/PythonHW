def missing_statues(statues):
    if not statues:
        return 0

    min_size = min(statues)
    max_size = max(statues)
    total_statues = set(range(min_size, max_size + 1))
    current_statues = set(statues)
    missing = total_statues - current_statues
    return len(missing)
