import argparse


parser = argparse.ArgumentParser(description="Script returns product of two numbers")
parser.add_argument('number', type=float, nargs=2, help='- two numbers')
args = parser.parse_args()
prod = args.number[0]*args.number[1]
if prod.is_integer():
    prod = int(prod)
print("The product is equal to", prod)
