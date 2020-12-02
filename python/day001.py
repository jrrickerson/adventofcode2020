'''Advent of Code 2020
   Day 1 Solution
'''
import functools
import operator


def noop(v):
    ''' No-op transform function that simply returns its value unchanged'''
    return v


def build_index(lines, transform=None):
    '''Build a dict index of values to line number, transforming the values
    via the transform function if provided'''
    transform = transform or noop
    lines = lines.split()
    return {transform(line.strip()): index for index, line in enumerate(lines)}


def find_factors(index, target_sum, num_factors=2, exclude=[]):
    '''Using an index dict, find two values that sum to a target value'''
    factors = []
    candidates = [k for k in index.keys() if k not in exclude]
    for key in candidates:
        looking_for = target_sum - key
        if num_factors > 2:
            sub_factors = find_factors(
                index, looking_for,
                num_factors=num_factors-1,
                exclude=exclude + [key])
            if sub_factors:
                factors = [key] + sub_factors
                break
        elif looking_for in index:
            factors = [key, looking_for]
            break
    else:
        return []
    return factors


def solve(filename, target):
    with open(filename) as f:
        index = build_index(f.read(), transform=int)
    num1, num2 = find_factors(index, 2020)
    return num1 * num2


def solve2(filename, target):
    with open(filename) as f:
        index = build_index(f.read(), transform=int)
    factors = find_factors(index, 2020, num_factors=3)
    return functools.reduce(operator.mul, factors)


if __name__ == '__main__':
    solution = solve('data/day001.in', 2020)
    print('Day 001 (Part 1): ', solution)
    solution2 = solve2('data/day001.in', 2020)
    print('Day 001 (Part 2): ', solution2)
