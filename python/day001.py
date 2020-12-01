'''Advent of Code 2020
   Day 1 Solution
'''


def noop(v):
    ''' No-op transform function that simply returns its value unchanged'''
    return v


def build_index(lines, transform=None):
    '''Build a dict index of values to line number, transforming the values
    via the transform function if provided'''
    transform = transform or noop
    lines = lines.split()
    return {transform(line.strip()): index for index, line in enumerate(lines)}


def find_factors(index, target_sum):
    '''Using an index dict, find two values that sum to a target value'''
    for key in index.keys():
        looking_for = target_sum - key
        if looking_for in index:
            break
    else:
        return 0, 0
    return key, looking_for


def solve(filename, target):
    with open(filename) as f:
        index = build_index(f.read(), transform=int)
    num1, num2 = find_factors(index, 2020)
    return num1 * num2


if __name__ == '__main__':
    solution = solve('data/day001.in', 2020)
    print('Day 001: ', solution)
