from functools import reduce
from sys import stdin


def star1(lines):
    s = 0
    for _, output_value in lines:
        s += len([
            signal for signal in output_value if len(signal) in [2, 4, 3, 7]
        ])
    return s


def star2(lines):
    s = 0
    for signals, output_value in lines:
        signals = [set(signal) for signal in signals]
        signals.sort(key=len)

        digits = {}

        digits[1] = signals[0]
        digits[7] = signals[1]
        digits[4] = signals[2]
        digits[8] = signals[-1]

        bd = digits[4] - digits[1]
        eg = digits[8] - (digits[4] | digits[7])
        cde = digits[8] - reduce(set.intersection, signals[6:9])
        g = eg - cde
        digits[9] = digits[4] | digits[7] | g

        e = digits[8] - digits[9]
        c = cde - bd - e
        d = cde - e - c

        digits[5] = digits[9] - c
        digits[0] = digits[8] - d

        b = digits[0] & bd
        digits[3] = digits[8] - b - e
        digits[6] = digits[8] - c
        f = digits[1] - c
        digits[2] = digits[8] - b - f

        digits = {digit: ''.join(sorted(signal)) for digit, signal in digits.items()}
        signal_to_digit = {signal: digit for digit, signal in digits.items()}

        output_value = [''.join(sorted(signal)) for signal in output_value]
        output_value = [signal_to_digit[value] for value in output_value]

        output_int = int(''.join(map(str, output_value)))
        s += output_int

    return s


if __name__ == '__main__':
    lines = [line.rstrip().split('|') for line in stdin.readlines()]
    lines = [
        (signals, output_value)
        for signals, output_value in map(lambda x: map(str.split, x), lines)
    ]

    print(star1(lines), end='\n\n')
    print(star2(lines))
