import argparse


def check_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    return "odd"


parser = argparse.ArgumentParser(description="Script gets the number and outputs whether it is even or not")
parser.add_argument("number", type=int, help="- number whose parity is to be determined")
args = parser.parse_args()
print(f"The number {args.number} is", check_even_or_odd(args.number))
