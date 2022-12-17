from copy import deepcopy


class Grid:
    def __init__(self, grid):
        self.grid = deepcopy(grid)
        self.y_len = len(grid)
        self.x_len = len(grid)

    def __out_of_bounds(self, x, y):
        return not (0 <= x < self.x_len and 0 <= y < self.y_len)

    def get(self, x, y):
        return self.grid[y][x]

    def set(self, x, y, value):
        self.grid[y][x] = value

    def update(self, x, y, f):
        self.grid[y][x] = f(self.grid[y][x])

    def get_adjacent_coords(self, x, y, include_diagonals=False):
        adjacent_coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        diagonals = [(x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]
        if include_diagonals:
            adjacent_coords += diagonals
        return [
            (x, y) for (x, y) in adjacent_coords
            if not self.__out_of_bounds(x, y)
        ]

    def get_adjacent_values(self, x, y):
        return [
            self.grid[y][x] for (x, y) in self.get_adjacent_coords(x, y)
        ]

    def all_coords(self):
        for y in range(self.y_len):
            for x in range(self.x_len):
                yield (x, y)

    # def __iter__(self):
    #     self.iter_index = 0
    #     return self

    # def __next__(self):
    #     if self.iter_index >= self.__y_len * self.__x_len:
    #         pass
    #     else:
    #         raise StopIteration

    def __getitem__(self, y):
        return self.grid[y]

    def __repr__(self):
        s = ''
        for row in self.grid:
            s += ' '.join(map(str, row)) + '\n'
        return s
