from sys import stdin
import re


def fold_paper(dots, axis, fold_pos):
    # axis = 0 if axis == 'x' else 1
    dots_to_add = set()
    dots_to_remove = set()
    for x, y in dots:
        if axis == 'x' and x > fold_pos:
            new_pos = (fold_pos * 2 - x, y)
            dots_to_add.add(new_pos)
            dots_to_remove.add((x, y))
        if axis == 'y' and y > fold_pos:
            new_pos = (x, fold_pos * 2 - y)
            dots_to_add.add(new_pos)
            dots_to_remove.add((x, y))
    for dot in dots_to_remove:
        dots.remove(dot)
    for dot in dots_to_add:
        dots.add(dot)


def star1(dots, folds):
    axis, fold_pos = folds[0]
    fold_paper(dots, axis, fold_pos)
    return len(dots)


def print_paper(dots):
    x_max = 0
    y_max = 0
    for x, y in dots:
        x_max = max(x, x_max)
        y_max = max(y, y_max)
    x_max += 1
    y_max += 1
    s = ''
    for y in range(y_max):
        s += ''.join(['#' if (x, y) in dots else ' ' for x in range(x_max)]) + '\n'
    return s


def star2(dots, folds):
    for axis, fold_pos in folds:
        fold_paper(dots, axis, fold_pos)
    return print_paper(dots)


def read_input():
    dots = set()
    while (line := stdin.readline()) != '\n':
        x, y = map(int, line.split(','))
        dots.add((x, y))
    folds = []
    while line := stdin.readline():
        match = re.match(r'fold along (.)=(\d+)', line).groups()  # type: ignore
        axis, fold_pos = match
        folds.append((axis, int(fold_pos)))
    return (dots, folds)


if __name__ == '__main__':
    dots, folds = read_input()

    print(star1(dots, folds), end='\n\n')
    print(star2(dots, folds))
