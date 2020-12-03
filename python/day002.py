'''Advent of Code 2020
   Day 2 Solution - Password Philosophy
'''
import re


def parse_record(line):
    try:
        policy, password = line.split(': ')
    except ValueError:
        return '', ''
    return policy.strip(), password.strip()


def parse_policy(policy):
    try:
        value_range, character = policy.split()
        lower, upper = value_range.strip().split('-')
        return int(lower), int(upper), character
    except ValueError:
        return 0, 0, ''


def count_valid_passwords(records):
    valid = 0
    for record in records:
        policy, password = parse_record(record)
        if not (password and policy):
            continue
        lower, upper, character = parse_policy(policy)
        if not all((lower, upper, character)):
            continue
        if lower <= password.count(character) <= upper:
            valid += 1

    return valid


def solve(filename):
    with open(filename) as f:
        lines = f.readlines()
    return count_valid_passwords(lines)


if __name__ == '__main__':
    solution = solve('data/day002.in')
    print('Day 002 (Part 1): ', solution)
