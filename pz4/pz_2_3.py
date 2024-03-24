import argparse


parser = argparse.ArgumentParser(description="Script receives a set of strings "
                                             "and returns the result of concatenation of all strings")
parser.add_argument("strings", nargs="+", help="- input strings")
args = parser.parse_args()
print("Concatenated string -", ''.join(args.string))
