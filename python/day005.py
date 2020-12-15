'''Advent of Code 2020
   Day 5 Solution - Binary Boarding
'''


def to_binary_sequence(string, onchars=''):
    '''Given a string, convert it to a binary list of integers, where any character
    in the "onchars" parameter is mapped to a 1, and everything else is a 0'''
    return [1 if char in onchars else 0 for char in string]


def binary_partition(sequence, range_max):
    '''Recursive binary partitioning algorithm.
    Given a sequence of integers 0 or 1, and a maximum range, find the integer
    within the range indicating by the binary partitioning sequence'''
    return (
        range_max // 2 * sequence[0] +
        binary_partition(sequence[1:], range_max // 2)
        if sequence else 0)


def part_one(passes, rows, cols):
    seat_ids = []
    for boarding_pass in passes:
        boarding_pass = boarding_pass.strip()
        row = binary_partition(
            to_binary_sequence(boarding_pass[:7], onchars='B'), rows)
        col = binary_partition(
            to_binary_sequence(boarding_pass[7:], onchars='R'), cols)
        seat_ids.append(row * 8 + col)
    return max(seat_ids)


def part_two():
    pass


def solve(filename):
    with open(filename) as f:
        solution = part_one(f, rows=128, cols=8)
    print('Day 005 (Part 1): ', solution)


if __name__ == '__main__':
    solve('data/day005.in')
