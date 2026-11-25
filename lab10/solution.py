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

def matrix_vector_product(matrix : list[list[float]], vector : list[float]) -> list[float]:
    a = np.array(matrix)
    b = np.array(vector)
    c = a @ b
    return c.tolist()

def matrix_multiply(left : list[list[float]], right : list[list[float]] -> list[list[float]]):
    a = np.array(left)
    b = np.array(right)
    c = a @ b
    return c.tolist()

def transpose_matrix(matrix : list[list[float]]) -> list[list[float]]:
    a = np.array(matrix)
    b = a.T
    return b.tolist()
