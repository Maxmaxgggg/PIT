import argparse
import math


def are_nums_coprime(num1, num2):
    gcd = math.gcd(num1, num2)
    if gcd == 1 or gcd == -1:
        return "are coprime"
    return "are not coprime"


parser = argparse.ArgumentParser(description="Script receives two numbers and returns whether they are coprime or not")
parser.add_argument("numbers", type=int, nargs=2, help="- two numbers")
args = parser.parse_args()
print(f"Numbers {args.numbers[0]} and {args.numbers[1]}", are_nums_coprime(args.numbers[0], args.numbers[1]))
