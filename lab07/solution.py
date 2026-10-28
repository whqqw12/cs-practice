import numpy as np

def reshape_rows(values :  list[float], width : int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype = float)
    matrix = arr.reshape(-1, width)
    return matrix.tolist()

def block(matrix: list[list[float]], rows:list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix, dtype = float)
    result = arr[np.ix_(rows,ccolumns)]
    return result.tolist()

def column_means(matrix : list[list[float]]) -> list[float]:
    if len(matrix) == 0:
        return []
    arr = np.asarray(matrix, dtype=float)
    means = np.mean(arr, axis = 0)
    return np.round(means,6).tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    if len(matrix) == 0:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    values = arr[:, column]
    result = np.max(values) - np.min(values)
    return round(float(result), 6)
