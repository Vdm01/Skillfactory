#начальная пустая матрица
matrix = [["-" for j in range(3)] for i in range(3)]
#глобальная переменная для проверки условия продолжения программы (запроса на ввод данных)
_continue = True


#функция для вывода построчно элементов матрицы
def print_matrix():
    for i in matrix:
        print(i)


#вывод начальной матрицы
print_matrix()


#функция для запроса на ввод координат для крестика
def input_cross():
    global _continue
    x = int(input("Введите координату x для крестика (от 0 до 2): "))
    y = int(input("Введите координату y для крестика (от 0 до 2): "))
    if coordinates_check(x, y): #вызов функции для проверки правильности ввода координат
        matrix[x][y] = "X"
        print_matrix()
        if win_check_cross(matrix): #вызов функции для проверки условий победы
            print("Крестики победили!")
            _continue = False
            exit()
    else:
        print("Координаты введены неправильно. Введите ещё раз: ")
        input_cross()


#функция для запроса на ввод координат для нолика
def input_zero():
    global _continue
    x = int(input("Введите координату x для нолика (от 0 до 2): "))
    y = int(input("Введите координату y для нолика (от 0 до 2): "))
    if coordinates_check(x, y): #вызов функции для проверки правильности ввода координат
        matrix[x][y] = "O"
        print_matrix()
        if win_check_zero(matrix): #вызов функции для проверки условий победы
            print("Нолики победили!")
            _continue = False
            exit()
    else:
        print("Координаты введены неправильно. Введите ещё раз: ")
        input_zero()


#функция для проверки правильности ввода координат
def coordinates_check(x, y):
    if (0 <= x <= 2) and (0 <= y <= 2): #сначала проверка на вхождение в нужный диапазон
        if all([matrix[x][y] != "X", #потом проверка на уже введёные координаты (реализовано через all)
                matrix[x][y] != "O",]):
            return True


#функции для проверки условий победы
#все крестики по вертикали, горизонтали и диагонали
def win_check_cross(matrix):
    if any([matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X",
            matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X",
            matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X",
            matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X",
            matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X",
            matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X",
            matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X",
            matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X"]):
        return True


#все нолики по вертикали, горизонтали и диагонали
def win_check_zero(matrix):
    if any([matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O",
            matrix[1][0] == "O" and matrix[1][1] == "O" and matrix[1][2] == "O",
            matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O",
            matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O",
            matrix[0][1] == "O" and matrix[1][1] == "O" and matrix[2][1] == "O",
            matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O",
            matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O",
            matrix[0][2] == "O" and matrix[1][1] == "O" and matrix[2][0] == "O"]):
        return True


#вызов функций для ввода координат крестиков и ноликов
while _continue:
    input_cross()
    input_zero()
