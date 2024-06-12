import argparse

parser = argparse.ArgumentParser(description="Скрипт принимает неотрицательное нечетное число "
                                             "и возвращает квадрат этого размера")
parser.add_argument('size', metavar="размер", help='- размер магического квадрата', type=int)
args = parser.parse_args()


def create_magic_square(n):
    # Создается квадратный список magic_square размера n x n, заполненный нулями.
    magic_square = [[0] * n for _ in range(n)]
    # Инициализируются переменные num, i и j. num - это число, которое мы будем помещать в квадрат.
    # i и j - это начальные координаты для размещения num в квадрате.
    num = 1
    # Мы начинаем с верхней середины квадрата (i = 0, j = n // 2).
    i, j = 0, n // 2
    # Запускается цикл, который продолжается, пока мы
    # не заполним весь квадрат значениями от 1 до n^2
    while num <= n * n:
        # В каждой итерации цикла текущее значение num помещается в ячейку с координатами (i, j).
        magic_square[i][j] = num
        num += 1
        # Затем определяются новые координаты (newi, newj) для следующего значения num. Эти новые координаты находятся выше и справа от текущей позиции (i, j) соответственно. Если новые координаты выходят за границы квадрата,
        # они переходят на противоположную сторону (по модулю n).
        newi, newj = (i - 1) % n, (j + 1) % n
        # Проверяется, занята ли ячейка с новыми координатами (newi, newj). Если она занята (т.е. содержит ненулевое значение), то сдвигаемся влево от текущей позиции, уменьшая j на 1.
        # Иначе мы переходим к новым координатам (newi, newj).
        if magic_square[newi][newj]:
            j = (j - 1) % n
        else:
            i, j = newi, newj
    return magic_square


def print_magic_square(square):
    # Определение максимальной длины числа в квадрате
    max_length = len(str(len(square[1])*len(square[1])))

    # Печать квадрата
    for row in square:
        for num in row:
            # Форматирование числа с выравниванием по правому краю
            print("{:^{}}".format(num, max_length), end=" ")
        print()


def main() -> None:
    if args.size < 3:
        print('Число не может быть меньше 3')
        exit()
    if args.size % 2 == 0:
        print('Число должно быть нечетным')
        exit()
    magic_square = create_magic_square(args.size)

    print(f"Магический квадрат размера {args.size}: ")
    print_magic_square(magic_square)


if __name__ == '__main__':
    main()