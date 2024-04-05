import argparse


# Функции для определения подъезда, этажа и порядка квартиры
def get_ent(num):
    if num % 54 == 0:
        return num//54
    return num//54 + 1


def get_fl(num):
    floor = num - (get_ent(num) - 1) * 54
    if floor % 6 == 0:
        return floor//6
    return floor//6 + 1


def get_ap(num):
    return num - (get_ent(num) - 1)*54 - (get_fl(num) - 1)*6


parser = argparse.ArgumentParser(description="Script receives apartment number and outputs apartment location")
parser.add_argument("ap_num", type=int, help='- apartment number from [1,216]')
args = parser.parse_args()
try:
    assert 1 <= args.ap_num <= 216, "Wrong apartment number"
except AssertionError as error:
    print(error)
    exit()
print(f'Номер квартиры: {args.ap_num} | Подъезд: {get_ent(args.ap_num)} '
      f'| Этаж: {get_fl(args.ap_num)} | Порядок: {get_ap(args.ap_num)}')
