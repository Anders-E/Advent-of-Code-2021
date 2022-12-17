from sys import stdin
from math import prod


version_sum = 0


def read_bits(packet, n):
    val = int(''.join(packet[:n]), 2)
    del packet[:n]
    return val


def read_version_and_type(packet):
    version = read_bits(packet, 3)
    global version_sum
    version_sum += version
    type_id = read_bits(packet, 3)
    return version, type_id


def read_length_0(packet):
    values = []
    subpackets_len = read_bits(packet, 15)
    bits_read = 0
    while bits_read < subpackets_len:
        length = len(packet)
        values.append(read_packet(packet))
        bits_read += length - len(packet)
    return values


def read_length_1(packet):
    values = []
    no_of_subpackets = read_bits(packet, 11)
    for _ in range(no_of_subpackets):
        values.append(read_packet(packet))
    return values


def read_literal(packet):
    val = []
    pos = 0
    bits = packet[pos:pos+5]
    while bits and bits[0] == '1':
        val += bits[1:]
        pos += 5
        bits = packet[pos:pos+5]
    val += bits[1:]
    pos += 5
    bits = packet[pos:pos+5]
    del packet[:pos]
    return int(''.join(val), 2)


def op(type_id, values):
    if type_id == 0:
        return sum(values)
    if type_id == 1:
        return prod(values)
    if type_id == 2:
        return min(values)
    if type_id == 3:
        return max(values)
    if type_id == 5:
        return int(values[0] > values[1])
    if type_id == 6:
        return int(values[0] < values[1])
    if type_id == 7:
        return int(values[0] == values[1])


def read_packet(packet):
    _, type_id = read_version_and_type(packet)

    if type_id != 4:
        length_type_id = read_bits(packet, 1)
        values = read_length_1(packet) if length_type_id else read_length_0(packet)
        return op(type_id, values)
    else:  # literal
        return read_literal(packet)


def star1(hexstring):
    s = ''
    for c in hexstring:
        s += format(int(c, 16), '04b')
    s = list(s)
    read_packet(s)
    return version_sum


def star2(hexstring):
    s = ''
    for c in hexstring:
        s += format(int(c, 16), '04b')
    s = list(s)
    return read_packet(s)


if __name__ == '__main__':
    hexstring = stdin.readline()

    print(star1(hexstring), end='\n\n')
    print(star2(hexstring))
