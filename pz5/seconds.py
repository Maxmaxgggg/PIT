import argparse

parser = argparse.ArgumentParser(description="Script receives number of seconds"
                                             " and outputs the time in 'hh:mm:ss' format")
parser.add_argument("seconds", type=int, help='- number of seconds')
args = parser.parse_args()
try:
    assert args.seconds >= 0, "Number of seconds must be positive"
except AssertionError as error:
    print(error)
    exit()
hours = args.seconds//3600
minutes = args.seconds//60 - hours * 60
seconds = args.seconds - hours * 3600 - minutes * 60
print('Time is:', '{:02d}:{:02d}:{:02d}'.format(hours % 24, minutes, seconds))
