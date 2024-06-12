import argparse
from itertools import permutations

parser = argparse.ArgumentParser(description="Скрипт генерирует все перестановки букв в переданном слове")
parser.add_argument("word", metavar="слово", type=str,
                    help="- слово, для букв которого необходимо сгенерировать все перестановки")
args = parser.parse_args()
comb_list = [''.join(perm) for perm in permutations(args.word)]
print('Перестановки букв слова "', args.word, '": ', ', '.join(comb_list), sep='')
