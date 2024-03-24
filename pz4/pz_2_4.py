import argparse
import math


parser = argparse.ArgumentParser(description="Script receives two numbers and returns their gcd")
parser.add_argument("number", type=int, nargs=2, help="- numbers for the gcd")
args = parser.parse_args()
print(f"The gcd of {args.number[0]} and {args.number[1]} is", math.gcd(args.number[0], args.number[1]))
