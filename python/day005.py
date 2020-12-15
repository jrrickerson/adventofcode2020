"""Advent of Code 2020
   Day 5 Solution - Binary Boarding
"""


def to_binary_sequence(string, onchars=""):
    """Given a string, convert it to a binary list of integers, where any character
    in the "onchars" parameter is mapped to a 1, and everything else is a 0"""
    return [1 if char in onchars else 0 for char in string]


def binary_partition(sequence, range_max):
    """Recursive binary partitioning algorithm.
    Given a sequence of integers 0 or 1, and a maximum range, find the integer
    within the range indicating by the binary partitioning sequence"""
    return (
        range_max // 2 * sequence[0] + binary_partition(sequence[1:], range_max // 2)
        if sequence
        else 0
    )


def find_adjacent_subset(vacant, occupied):
    for seat_id in vacant:
        if {seat_id - 1, seat_id + 1} <= occupied:
            return seat_id
    return None


def part_one(passes, rows, cols):
    seat_ids = []
    for boarding_pass in passes:
        boarding_pass = boarding_pass.strip()
        row = binary_partition(to_binary_sequence(boarding_pass[:7], onchars="B"), rows)
        col = binary_partition(to_binary_sequence(boarding_pass[7:], onchars="R"), cols)
        seat_ids.append(row * 8 + col)
    return max(seat_ids)


def part_two(passes, rows, cols):
    all_seats = [x * 8 + y for x in range(128) for y in range(8)]
    taken_seats = []
    for boarding_pass in passes:
        boarding_pass = boarding_pass.strip()
        row = binary_partition(to_binary_sequence(boarding_pass[:7], onchars="B"), rows)
        col = binary_partition(to_binary_sequence(boarding_pass[7:], onchars="R"), cols)
        taken_seats.append(row * 8 + col)
    occupied = set(taken_seats)
    vacant_seats = set(all_seats) - occupied
    seat = find_adjacent_subset(vacant_seats, occupied)
    return seat


def solve(filename):
    with open(filename) as f:
        solution = part_one(f, rows=128, cols=8)
    print("Day 005 (Part 1): ", solution)
    with open(filename) as f:
        solution = part_two(f, rows=128, cols=8)
    print("Day 005 (Part 2): ", solution)


if __name__ == "__main__":
    solve("data/day005.in")
