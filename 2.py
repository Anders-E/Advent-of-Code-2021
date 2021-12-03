from sys import stdin
from functools import reduce

def move_submarine(pos, command):
    uses_aim = 'aim' in pos
    match command:
        case ['forward', x] if uses_aim:
            pos['x'] += x
            pos['y'] += x * pos['aim']
        case ['forward', x]:
            pos['x'] += x
        case ['down', x] if uses_aim:
            pos['aim'] += x
        case ['down', x]:
            pos['y'] += x
        case ['up', x] if uses_aim:
            pos['aim'] -= x
        case ['up', x]:
            pos['y'] -= x
    return pos

def calculate_pos(commands, start_pos={'x': 0, 'y': 0}):
    pos = reduce(move_submarine, commands, start_pos)
    return pos['x'] * pos['y'] 

def star1(commands):
    return calculate_pos(commands)

def star2(commands):
    return calculate_pos(commands, {'x': 0, 'y': 0, 'aim': 0})

if __name__ == '__main__':
    commands = [(direction, int(distance)) for (direction, distance) in map(str.split, stdin.readlines())]
    print(star1(commands), end='\n\n')
    print(star2(commands))
