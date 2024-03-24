import argparse


parser = argparse.ArgumentParser(description="Script receives a number as input and outputs whether it is prime or not")
parser.add_argument("number", type=int, help="- the number for which it is necessary to find out if it is prime")
args = parser.parse_args()
num = args.number
if num == 1:
    print("Number 1 is not prime by definition")
    exit()
for i in range(2, num//2+1):
    if num % i == 0:
        print(f"Number {num} is not prime")
        exit()
print(f"Number {num} is prime")
