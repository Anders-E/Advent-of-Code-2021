import heapq
import itertools
from sys import stdin
from collections import defaultdict
from math import inf

from datastructures.grid import Grid


# TODO: Move priority queue to separate file
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count


def add_task(q, task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(q, entry)


def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task(q):
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while q:
        priority, count, task = heapq.heappop(q)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


def shortest_path(grid, start_x, start_y):
    global entry_finder, REMOVED, counter
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count

    dist = defaultdict(lambda: inf)
    prev = {}
    dist[(start_x, start_y)] = 0

    q = []
    for v in grid.all_coords():
        add_task(q, v, dist[v])

    while entry_finder:
        u = pop_task(q)
        for v in grid.get_adjacent_coords(*u):
            if v not in entry_finder:
                continue
            risk = grid.get(*v)
            alt = dist[u] + risk
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                add_task(q, v, alt)
    return dist[(grid.x_len - 1, grid.y_len - 1)]


def extend_row(row, row_no):
    new_row = []
    length = len(row)
    for i in range(5):
        for n in row[:length]:
            new_value = n + i + row_no
            if new_value > 9:
                new_value -= 9
            new_row.append(new_value)
    return new_row


def extend_cave(cave):
    extended_cave = []
    length = len(cave)
    for i in range(5):
        for row in cave[:length]:
            new_row = extend_row(row, i)
            extended_cave.append(new_row)
    return extended_cave


def star1(cave):
    return shortest_path(cave, 0, 0)


def star2(cave):
    extended_cave = extend_cave(cave.grid)
    extended_cave = Grid(extended_cave)
    return shortest_path(extended_cave, 0, 0)


if __name__ == '__main__':
    extended_cave = [list(map(int, line.rstrip())) for line in stdin.readlines()]

    print(star1(Grid(extended_cave)), end='\n\n')
    print(star2(Grid(extended_cave)))
