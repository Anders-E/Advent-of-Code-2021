from sys import stdin
from math import prod

from datastructures.grid import Grid


def star1(heightmap):
    s = 0
    for x, y in heightmap.all_coords():
        height = heightmap[y][x]
        adjacents = heightmap.get_adjacent_values(x, y)
        low_point = all(adj > height for adj in adjacents)
        if low_point:
            s += height + 1
    return s


visited = set()


def measure_basin(heightmap, x, y, area=1):
    visited.add((x, y))

    adjacents_coords = heightmap.get_adjacent_coords(x, y)
    adjacents = [
        (adj_x, adj_y) for (adj_x, adj_y) in adjacents_coords
        if heightmap[adj_y][adj_x] > heightmap[y][x]
        and heightmap[adj_y][adj_x] != 9
    ]

    current_area = area
    for adj_x, adj_y in adjacents:
        if (adj_x, adj_y) in visited:
            continue
        area += measure_basin(heightmap, adj_x, adj_y, current_area)

    return area


def star2(heightmap):
    basin_sizes = []
    for x, y in heightmap.all_coords():
        height = heightmap[y][x]
        adjacents = heightmap.get_adjacent_values(x, y)
        low_point = all(adj > height for adj in adjacents)
        if low_point:
            basin_size = measure_basin(heightmap, x, y)
            basin_sizes.append(basin_size)
    return prod(sorted(basin_sizes)[-3:])


if __name__ == '__main__':
    heightmap = [list(map(int, line.rstrip())) for line in stdin.readlines()]
    heightmap = Grid(heightmap)

    print(star1(heightmap), end='\n\n')
    print(star2(heightmap))
