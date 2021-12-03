from sys import stdin
from collections import Counter


def star1(nums):
    bits_by_index = list(zip(*nums))  # transpose
    bit_counts = list(map(Counter, bits_by_index))
    gamma_bits = [
        '1' if count['1'] > count['0'] else '0' for count in bit_counts
    ]
    gamma = int(''.join(gamma_bits), 2)
    epsilon = ~gamma & 0xFFF

    return gamma * epsilon


def get_rating(nums, oxygen_rating=True):
    filtered_nums = nums[:]
    i = 0
    while len(filtered_nums) > 1:
        bit_counts = Counter([num[i] for num in filtered_nums])
        if oxygen_rating:
            accepted_bit = '1' if bit_counts['1'] >= bit_counts['0'] else '0'
        else:
            accepted_bit = '0' if bit_counts['0'] <= bit_counts['1'] else '1'
        filtered_nums = [x for x in filtered_nums if x[i] is accepted_bit]
        i += 1
    return int(filtered_nums[0], 2)


def star2(nums):
    oxygen_generator_rating = get_rating(nums)
    co2_scrubber_rating = get_rating(nums, False)
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == '__main__':
    nums = list(map(str.strip, stdin.readlines()))
    print(star1(nums), end='\n\n')
    print(star2(nums))
