import argparse


parse = argparse.ArgumentParser(description="Script receives list of strings and returns it without duplicates")
parse.add_argument("strings", nargs="+", help="- list of strings")
args = parse.parse_args()
print("List without duplicates:", ", ".join(list(set(args.strings))))
