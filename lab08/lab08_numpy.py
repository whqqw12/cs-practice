import numpy as np

#задание1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)


#задание2
print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Обратный порядок:", hours[::-1])


#задание3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("\nЗадание 3")
print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент:\n", temperatures[:2, 1:3])


#задание4
matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
print("Исходная матрица:\n", matrix)

part1 = matrix[:3, :]
part2 = matrix[-2:, :]
part3 = matrix[:, :2]
part4 = matrix[1:4, 2:5]
part5 = matrix[-2:, -2:]

print("Первые три строки:\n", part1)
print("shape:", part1.shape)

print("Последние две строки:\n", part2)
print("shape:", part2.shape)

print("Первые два столбца:\n", part3)
print("shape:", part3.shape)

print("Строки 1-3, столбцы 2-4:\n", part4)
print("shape:", part4.shape)

print("Правый нижний блок 2x2:\n", part5)
print("shape:", part5.shape)


#задание5
print("\nЗадание 5")

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("Измененный вектор:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("Измененная маленькая матрица:\n", small_matrix)

# copy() создает независимую копию массива,
# поэтому исходный hours не изменяется.
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("Измененный hours:", changed_hours)
print("Исходный hours:", hours)

# copy() сохраняет исходную матрицу без изменений.
changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Измененная матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)


#задание6
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("\nЗадание 6")
print("numbers:", numbers)
print("table:\n", table)
print("transposed:\n", transposed)

print("numbers shape:", numbers.shape)
print("table shape:", table.shape)
print("transposed shape:", transposed.shape)

