def winner(names: list[str], scores: list[float]) -> str:
    best = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best]:
            best = i
    return names[best]
