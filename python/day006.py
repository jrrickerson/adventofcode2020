"""Advent of Code 2020
   Day 6 Solution - Custom Customs
"""
import itertools


def parse_groups(data):
    """Given an iterable of lines of text (i.e. from a file), generate a group iterator
    which consists of all lines split by blank lines"""
    for k, g in itertools.groupby((line.strip() for line in data), bool):
        if k:
            yield list(g)


def count_answer_set_union(group):
    """Given a list of strings, find the union set of all characters in any string"""
    answer_set = set(itertools.chain.from_iterable(group))
    return len(answer_set)


def part_one(answer_data):
    """Get the sum of all lengths of the answer sets from any of the groups"""
    group_counts = []
    for answer_group in parse_groups(answer_data):
        group_counts.append(count_answer_set_union(answer_group))
    return sum(group_counts)


def solve(filename):
    with open(filename) as f:
        solution = part_one(f)
    print("Day 006 (Part 1): ", solution)


if __name__ == "__main__":
    solve("data/day006.in")
