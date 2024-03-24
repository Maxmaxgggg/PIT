import argparse


parser = argparse.ArgumentParser(description="Script receives a list of numbers and returns the largest one")
parser.add_argument("numbers", type=int, nargs="+", help="- input numbers")
args = parser.parse_args()
print("Largest element is", max(args.numbers))
