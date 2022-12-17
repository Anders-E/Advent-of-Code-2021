from sys import stdin


class Board:
    def __init__(self, board):
        self.__board = board
        self.__index_board()
        self.__marked = [[False] * 5 for _ in range(5)]
        self.bingo = False

    def __index_board(self):
        self.__index = {
            n: (x, y)
            for y, row in enumerate(self.__board)
            for x, n in enumerate(row)
        }

    def score(self, last_draw):
        s = sum([
            self.__board[y][x]
            for y in range(5) for x in range(5) if not self.__marked[y][x]
        ])
        return s * last_draw

    def mark(self, draw):
        if draw not in self.__index:
            return
        x, y = self.__index[draw]
        self.__marked[y][x] = True
        if not self.bingo:
            horizontal_bingo = all([self.__marked[y][x] for x in range(5)])
            vertical_bingo = all([self.__marked[y][x] for y in range(5)])
            self.bingo = horizontal_bingo or vertical_bingo


def star1(draws, boards):
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.bingo:
                return board.score(draw)


def star2(draws, boards):
    for draw in draws:
        for board in boards:
            board.mark(draw)
        if len(boards) == 1 and boards[0].bingo:
            return boards[0].score(draw)
        boards = [board for board in boards if not board.bingo]


def parse_board(input_lines):
    board = []
    for _ in range(5):
        row = list(map(int, input_lines.pop().split()))
        board.append(row)
    return board


def parse_input(input_lines):
    draws = map(int, input_lines.pop().split(','))
    boards = []
    while input_lines:
        input_lines.pop()
        boards.append(parse_board(input_lines))
    return draws, boards


if __name__ == '__main__':
    draws, boards = parse_input(list(reversed(stdin.readlines())))
    draws = list(draws)
    print(star1(draws, [Board(board) for board in boards]), end='\n\n')
    print(star2(draws, [Board(board) for board in boards]))
