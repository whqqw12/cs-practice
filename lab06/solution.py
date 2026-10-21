def count_items(values: list) -> dict:
    counts = {}
    for item in values:
        counts[item] = counts.get(item, 0) + 1
    return counts

