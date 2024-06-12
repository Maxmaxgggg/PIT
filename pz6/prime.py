import argparse


parser = argparse.ArgumentParser(description="Скрипт получает число и возвращает все простые делители этого числа")
parser.add_argument("number", type=int, nargs ="?", help="- число, для которого нужно вернуть все простые делители")
args = parser.parse_args()
