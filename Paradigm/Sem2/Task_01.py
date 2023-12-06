'''След матрицы - это сумма чисел на её главной диагонали. След определён только для квадратных матриц
(количество столбцов = количеству строк).

Задача
Реализовать чисто структурную реализацию вычисления следа для любой матрицы NxN.'''

matrix = [[1, 2, 3], [3, 2, 1], [6, 5, 2]]
trace = 0
for i in range(len(matrix[0])):
    trace += matrix[i][i]
print(trace)
print(*matrix)


'''процедурная реализация'''
def count_trace(matrix):
    trace = 0
    for i in range(len(matrix[0])):
        trace += matrix[i][i]
    return trace
print(count_trace(matrix))
