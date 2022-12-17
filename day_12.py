from sys import stdin
from collections import defaultdict


def find_paths(caves, current_cave, visited=set(), paths=[], path=[]):
    path = path + [current_cave]
    if current_cave == 'end':
        paths.append(path)
        return

    if current_cave.islower():
        visited.add(current_cave)

    next_caves = [cave for cave in caves[current_cave] if cave not in visited]
    for next_cave in next_caves:
        find_paths(caves, next_cave, visited, paths, path)

    if current_cave in visited:
        visited.remove(current_cave)

    return paths


def find_paths2(caves, current_cave, visited=defaultdict(int), paths=[], path=[]):
    path = path + [current_cave]
    if current_cave == 'end':
        paths.append(path)
        return

    if current_cave.islower() and current_cave != 'end':
        visited[current_cave] += 1

    double_visit = bool([val for val in visited.values() if val > 1])

    next_caves = [
        cave for cave in caves[current_cave]
        if (not double_visit and visited[cave] < 2) or
           (double_visit and visited[cave] < 1)
    ]
    for next_cave in next_caves:
        find_paths2(caves, next_cave, visited, paths, path)

    visited[current_cave] -= 1

    return paths


def star1(caves):
    paths = find_paths(caves, 'start')
    if paths:
        return len(paths)


def star2(caves):
    paths = find_paths2(caves, 'start')
    if paths:
        return len(paths)


def read_input():
    caves = defaultdict(list)
    for a, b in [s.split('-') for s in map(str.rstrip, stdin.readlines())]:
        if a != 'end' and b != 'start':
            caves[a].append(b)
        if a != 'start' and b != 'end':
            caves[b].append(a)
    return caves


if __name__ == '__main__':
    caves = read_input()
    print(star1(caves), end='\n\n')
    print(star2(caves))
