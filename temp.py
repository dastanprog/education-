import numpy as np

# Данные для примера 3
A = np.array([[2, -1, -4], [4, -9, 3], [2, -7, -1]])
B = np.array([[-4, 2, 1]])
C = np.array([[7, 1], [2, 1], [3, -3]])
D = np.array([[-1, 0], [1, 3], [8, -2]])

# a) 2C + 5D, C - 3D
result_a_1 = 2 * C + 5 * D
result_a_2 = C - 3 * D

# b) Инверсия матрицы B (если возможно)
try:
    B_inv_3 = np.linalg.inv(B)
except np.linalg.LinAlgError:
    B_inv_3 = "B3 не является обратимой матрицей"

# c) Умножение матриц AB и BC
result_c_AB_3 = np.dot(A, B.T)
result_c_BC_3 = np.dot(B, C)

# d) Обратная матрица для A (если возможно)
try:
    A_inv_3 = np.linalg.inv(A)
except np.linalg.LinAlgError:
    A_inv_3 = "A3 не является обратимой матрицей"

# Вывод результатов
print("a) 2C + 5D:", result_a_1)
print("a) C - 3D:", result_a_2)

print("\nИнверсия матрицы B:", B_inv_3)

print("\nAB (умножение A и B):", result_c_AB_3)
print("BC (умножение B и C):", result_c_BC_3)

print("\nОбратная матрица для A:", A_inv_3)
