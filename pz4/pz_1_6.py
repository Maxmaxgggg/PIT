import argparse


parser = argparse.ArgumentParser(description="Script receives string and returns it in reverse order")
parser.add_argument("string", help="- string to be displayed in reverse order")
args = parser.parse_args()
print(f"{args.string} in reverse order is", args.string[::-1])
