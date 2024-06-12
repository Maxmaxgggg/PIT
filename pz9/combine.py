import argparse
from itertools import combinations

parser = argparse.ArgumentParser(description="Скрипт генерирует все сочетания заданного набора символов заданной длины")
parser.add_argument("string", metavar="набор символов", type=str,
                    help="- набора символов, для которого необходимо сгенерировать все сочетания")
parser.add_argument("length", metavar="длина", type=int,
                    help="- длина сочетания")
args = parser.parse_args()
try:
    assert (args.length > 0)
except AssertionError:
    print("Ошибка, вы ввели отрицательную длину")
    exit(1)
try:
    assert (args.length <= len(args.string))
except AssertionError:
    print("Ошибка, длина сочетания, которое вы хотите сгенерировать, превышает длину строки")
    exit(1)
comb_list = [''.join(comb) for comb in combinations(args.string, args.length)]
print('Сочетания строки "', args.string, '" имеющие длину ', args.length, ': ', ', '.join(comb_list), sep='')
