import argparse


parser = argparse.ArgumentParser(description="Скрипт генерирует список простых чисел до заданного числа")
parser.add_argument("number", metavar="число", type=int,
                    help="- целое положительное число, до которого необходимо найти простые числа")
args = parser.parse_args()
try:
    assert (args.number > 0)
except AssertionError:
    print("Ошибка, введенное число отрицательно")
    exit(1)
prime_list = [num for num in range(2, args.number+1) if all(num % div != 0 for div in range(2, num//2 + 1))]
print("Все простые числа до ", args.number, ": ", ", ".join(map(str, prime_list)), sep="")
