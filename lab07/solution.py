import numpy as np

def reshape_rows(values :  list[float], width : int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype = float)
    matrix = arr.reshape(-1, width)
    return matrix.tolist()
print(reshape_rows([12,14.4,11,13,15.5,10.5], 3))
    
