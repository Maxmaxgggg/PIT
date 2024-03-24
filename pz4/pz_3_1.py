import argparse


def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num*factorial(num-1)


parser = argparse.ArgumentParser(description="Script receives number and returns its factorial")
parser.add_argument("number", type=int, help="- number for which it is necessary to find the factorial")
args = parser.parse_args()
print(f"Factorial of {args.number} equals", factorial(args.number))
