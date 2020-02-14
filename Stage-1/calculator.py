#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print('perameter error')
        exit()
    try:
        income = int(sys.argv[1])
    except ValueError:
        print('perameter error')
        exit()
    value = income - 5000
    if value <= 0:
        result = 0
    elif value <= 3000:
        result = value * 0.03 - 0
    elif value <= 12000:
        result = value * 0.1 - 210
    elif value <= 25000:
        result = value * 0.2 - 1410
    elif value <= 35000:
        result = value * 0.25 - 2660
    elif value <= 55000:
        result = value * 0.3 - 4410
    elif value <= 80000:
        result = value * 0.35 - 7160
    else:
        result = value * 0.45 - 15160
    print('{:.2f}'.format(result))

if __name__ == '__main__':
    main()
