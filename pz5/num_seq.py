import argparse


def num(k: int):
    if (k-1) % 3 == 0:
        return 1
    if (k-2) % 3 == 0:
        return (k+1)//30
    if k % 3 == 0:
        return (k//3) % 10


parser = argparse.ArgumentParser(description="Script receives integer and outputs sequence number")
parser.add_argument('k', type=int, help=' - positive integer from [1,150]')
args = parser.parse_args()
try:
    assert 1 <= args.k <= 150, "Wrong argument"
except AssertionError as error:
    print(error)
    exit()
print(f"The number {num(args.k)} is in the place of {args.k}")
