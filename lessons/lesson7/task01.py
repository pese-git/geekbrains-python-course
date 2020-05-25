# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        if not self.__validate(matrix):
            raise RuntimeError('Ошибка в размерности матрицы')
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __str__(self):
        s = ""
        for row in self.matrix:
            s += str(row) + '\n'
        return s.strip()

    def __add__(self, value):
        if self.rows != value.rows or self.columns != value.columns:
            raise RuntimeError('Матрицы должны быть одной размерности')
        new_matrix = []
        for i in range(0, self.rows):
            row = []
            for ii in range(0, self.columns):
                row.append(self.matrix[i][ii] + value.matrix[i][ii])
            new_matrix.append(row)
        return Matrix(matrix=new_matrix)

    def __validate(self, matrix):
        columns = - 1
        is_valid = True
        for r in matrix:
            if columns == -1:
                columns = len(r)
                continue
            if columns != len(r):
                is_valid = False
                break
        return is_valid


if __name__ == '__main__':
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    matrix_a = Matrix(matrix=a)
    print('Матрица A')
    print(matrix_a)
    print(matrix_a.rows, 'x', matrix_a.columns)

    print('Матрица B')
    matrix_b = Matrix(matrix=b)
    print(matrix_b)
    print(matrix_b.rows, 'x', matrix_b.columns)

    print('Матрица C')
    matrix_c = matrix_a + matrix_b
    print(matrix_c)
    print(matrix_c.rows, 'x', matrix_c.columns)
