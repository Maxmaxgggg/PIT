import argparse


parser = argparse.ArgumentParser(description="Script receives a string as input and returns its length")
parser.add_argument("string", help="- string whose length is to be found")
args = parser.parse_args()
print("String length is", len(args.string))
