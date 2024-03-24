import argparse


def is_str_a_palindrome(input_string):
    string = input_string.replace(" ", "").lower()
    if string == string[::-1]:
        return "is a palindrome"
    return "is not a palindrome"


parser = argparse.ArgumentParser(description="Script receives a string and returns whether it is a palindrome")
parser.add_argument("string", help="- the string for which you want to determine if it is a palindrome")
args = parser.parse_args()
print(f'The string "{args.string}"', is_str_a_palindrome(args.string))
