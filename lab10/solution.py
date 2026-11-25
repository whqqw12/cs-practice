from numpy import *

def make_tables(rows : int, columns : int) -> list[list[int]]:
    a = np.arange(rows*columns)
    a = a.reshape(rows,columns)
    return a.tolist()

def rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int) -> list[list[float]]:
    a = np.array(matrix)
    b = a[row_start:row_stop,column_start:column_stop]
    return b.tolist()

def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int, column_start: int, column_stop: int, value: float) -> list[list[float]]:
    a = np.array(matrix,dtype=float).copy()
    a[row_start:row_stop,column_start:column_stop] = value
    return a.tolist()
