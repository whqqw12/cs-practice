def winner(names: list[str], scores: list[float]) -> str:
    best = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best]:
            best = i
    return names[best]

def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0
    total = sum(scores)
    result = total / len(scores)
    return round(result, 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    indexes = list(range(len(scores)))
    indexes.sort(key=lambda i: scores[i], reverse=True)
    result = []
    for i in indexes:
        result.append(names[i])
    return result
