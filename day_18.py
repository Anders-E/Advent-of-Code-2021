from sys import stdin


class SnailfishNumber:
    def __init__(self, left=None, right=None):
        self.left = left
        if self.left and not isinstance(self.left, int):
            self.left.parent = self
            self.left.leftChild = True
        self.right = right
        if self.right and not isinstance(self.right, int):
            self.right.parent = self
            self.right.leftChild = False

    def get_left_neighbor(self):
        return 0

    # def get_right_neighbor(self):
    #     if self.parent and isinstance(self.parent.right, int) and self.parent.right != self:
    #         return self.parent.right
    #     elif self.parent and self.parent.right and self.parent.right != self:
    #         return self.parent.right.get_leftmost()
    #     return 0

    def reduce(self, depth=0):
        # if depth == 4:
        # self.explode()
        if self.left and not isinstance(self.left, int):
            self.left.reduce(depth + 1)
        if self.right and not isinstance(self.right, int):
            self.right.reduce(depth + 1)
        return self

    def get_leftmost(self):
        if self.left and not isinstance(self.left, int):
            return self.left.get_leftmost()
        elif self.left:
            return self.left
        return self

    def get_rightmost(self):
        if self.right and not isinstance(self.right, int):
            return self.right.get_rightmost()
        elif self.right:
            return self.right
        return self

    def __repr__(self):
        s = '['
        if self.left:
            s += str(self.left)
        if self.right:
            s += f',{str(self.right)}'
        s += ']'
        return s

    def __add__(self, other):
        return SnailfishNumber(self, other)


def parse_number(tokens):
    tokens.pop()  # r bracket
    right = parse_number(tokens) if tokens[-1] == ']' else int(tokens.pop())
    tokens.pop()  # comma
    left = parse_number(tokens) if tokens[-1] == ']' else int(tokens.pop())
    tokens.pop()  # l bracket
    return SnailfishNumber(left, right)


def star1(snailfish_numbers):
    # for num in snailfish_numbers:
    #     print(num)

    # return snailfish_numbers[0] + snailfish_numbers[1]
    return snailfish_numbers[0].reduce()


def star2(snailfish_numbers):
    pass


if __name__ == '__main__':
    snailfish_numbers = [
        parse_number(list(line.rstrip()))
        for line in stdin.readlines()
    ]

    print(star1(snailfish_numbers), end='\n\n')
    print(star2(None))
