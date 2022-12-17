from sys import stdin
from itertools import filterfalse


def check_corrupt_line(line, repair=False):
    opening_to_closing = {'(': ')', '[': ']', '{': '}', '<': '>'}
    closing_to_opening = {v: k for (k, v) in opening_to_closing.items()}
    error_values = {')': 3, ']': 57, '}': 1197, '>': 25137}
    q = []
    for c in line:
        match c:
            case opening if opening in opening_to_closing:
                q.append(opening)
            case closing if closing in opening_to_closing.values():
                if q[-1] == closing_to_opening[closing]:
                    q.pop()
                else:
                    return error_values[closing]

    if repair:
        return repair_score([opening_to_closing[c] for c in reversed(q)])

    return 0


def repair_score(q):
    score = 0
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    for c in q:
        score *= 5
        score += scores[c]
    return score


def star1(navigation_subsystem):
    return sum(check_corrupt_line(line) for line in navigation_subsystem)


def star2(navigation_subsystem):
    incomplete_lines = filterfalse(check_corrupt_line, navigation_subsystem)
    repair_scores = [
        check_corrupt_line(line, True) for line in incomplete_lines
    ]
    sorted_scores = sorted(repair_scores)
    return sorted_scores[len(sorted_scores) // 2]


if __name__ == '__main__':
    navigation_subsystem = list(map(str.rstrip, stdin.readlines()))

    print(star1(navigation_subsystem), end='\n\n')
    print(star2(navigation_subsystem))
