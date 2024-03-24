import argparse


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


parser = argparse.ArgumentParser(description='Script receives as input a list of floating-point numbers'
                                             ' and returns their arithmetic mean')
parser.add_argument('number', type=float, nargs='+', help='- list of floating point numbers')
args = parser.parse_args()
avg = calculate_average(args.number)
print("The arithmetic mean is equal to", avg)
