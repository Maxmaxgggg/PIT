import argparse


parser = argparse.ArgumentParser(description="Script returns sum of two numbers")
parser.add_argument('number', type=float, nargs=2, help='- two numbers')
args = parser.parse_args()
result = sum(args.number)
if result.is_integer():
    result = int(result)
print("Sum is equal to", result)
