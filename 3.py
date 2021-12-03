from sys import stdin

def star1(nums):
    gamma = 0
    epsilon = 0

    return list(nums)

def star2(nums):
    pass

if __name__ == '__main__':
    nums = map(lambda n: int(n, 2), stdin.readlines())
    print(star1(nums), end='\n\n')
    print(star2(nums))
