from sys import stdin

from datastructures.grid import Grid
from util import inc


def flash(octopuses, x, y, has_flashed):
    if (x, y) in has_flashed:
        return
    has_flashed.add((x, y))
    for x, y in octopuses.get_adjacent_coords(x, y, True):
        octopuses.update(x, y, inc)
        energy_level = octopuses.get(x, y)
        if energy_level > 9:
            flash(octopuses, x, y, has_flashed)


def step(octopuses):
    has_flashed = set()
    for x, y in octopuses.all_coords():
        octopuses.update(x, y, inc)
        energy_level = octopuses.get(x, y)
        if energy_level > 9:
            flash(octopuses, x, y, has_flashed)
    for x, y in octopuses.all_coords():
        if octopuses.get(x, y) > 9:
            octopuses.set(x, y, 0)
    return len(has_flashed)


def star1(octopuses):
    total_flashes = 0
    for _ in range(100):
        total_flashes += step(octopuses)
    return total_flashes


def star2(octopuses):
    step_no = 0
    no_of_octopuses = octopuses.x_len * octopuses.y_len
    while True:
        step_no += 1
        flashes = step(octopuses)
        if flashes == no_of_octopuses:
            return step_no


if __name__ == '__main__':
    octopuses = [list(map(int, line.rstrip())) for line in stdin.readlines()]

    print(star1(Grid(octopuses)), end='\n\n')
    print(star2(Grid(octopuses)))
