import argparse


parser = argparse.ArgumentParser(description="Скрипт создает список всех палиндромов из переданного списка слов")
parser.add_argument("word_list", nargs="+", metavar="список слов", type=str,
                    help="- список слов, в котором необходимо найти палиндромы")
args = parser.parse_args()
palindrome_list = [word for word in args.word_list if word[::-1].lower().replace(" ", "") == word.lower().replace(" ", "")]
print("Все палиндромы из исходного списка :", ", ".join(palindrome_list))
