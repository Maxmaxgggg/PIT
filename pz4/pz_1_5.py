import argparse


parser = argparse.ArgumentParser(description="Script receives a list of integers and outputs their sum")
parser.add_argument('number', type=int, nargs='+', help='- list of integers')
args = parser.parse_args()
print("Sum is equal to", sum(args.number))
