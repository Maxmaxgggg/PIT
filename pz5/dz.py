import argparse
import re


# Функции, которые преобразуют углы во время и наоборот
def angles_to_time(h_ang: int, m_ang: int, s_ang: int):
    hrs = int(h_ang / 30) % 12
    mnt = int(m_ang / 6) % 60
    sec = int(s_ang / 6) % 60
    return '{:02d}:{:02d}:{:02d}'.format(hrs, mnt, sec)


def time_to_angles(time: str):
    hrs, mnt, sec = map(int, time.split(':'))
    h_ang = (hrs % 12) * 30 + (mnt / 60) * 30
    m_ang = (mnt / 60) * 360
    s_ang = (sec / 60) * 360
    return h_ang, m_ang, s_ang


parser = argparse.ArgumentParser(description='Script receives angles and outputs time or vice versa')
group = parser.add_mutually_exclusive_group()
group.add_argument('--time', '-t', type=str, help='use this flag to convert time into angles')
group.add_argument('--angle', '-a', nargs=3, type=int, help='use this flag to convert angles into time')
args = parser.parse_args()
# Проверяем, что включен один из флагов
try:
    assert args.time or args.angle, 'None of the flags are enabled'
except AssertionError as error:
    print(error)
    exit()

# Если преобразуем время в углы
if args.time:
    pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$')
    match = pattern.match(args.time)
    try:
        assert match, f'The string "{args.time}" does not have the correct time format'
    except AssertionError as error:
        print(error)
        exit()
    print(f'Hour angle is {time_to_angles(args.time)[0]}\u00b0, minute angle is {time_to_angles(args.time)[1]}\u00b0, '
          f'second angle is {time_to_angles(args.time)[2]}\u00b0')
# Если преобразуем углы во время
if args.angle:
    hours_ang = args.angle[0]
    minutes_ang = args.angle[1]
    seconds_ang = args.angle[2]
    try:
        assert hours_ang > 0 and minutes_ang > 0 and seconds_ang > 0, "Angles can't be negative"
    except AssertionError as error:
        print(error)
        exit()
    print("Time is:", angles_to_time(hours_ang, minutes_ang, seconds_ang))
