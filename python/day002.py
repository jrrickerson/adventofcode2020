"""Advent of Code 2020
   Day 2 Solution - Password Philosophy
"""
import re


def parse_record(line):
    try:
        policy, password = line.split(": ")
    except ValueError:
        return "", ""
    return policy.strip(), password.strip()


def parse_policy(policy):
    try:
        value_range, character = policy.split()
        lower, upper = value_range.strip().split("-")
        return int(lower), int(upper), character
    except ValueError:
        return 0, 0, ""


def validate_password_by_count(password, character, lower, upper):
    return lower <= password.count(character) <= upper


def validate_password_by_index(password, character, *positions):
    found_chars = [password[pos - 1] == character for pos in positions]
    return found_chars.count(True) == 1


def count_valid_passwords(records, use_index=False):
    count = 0
    for record in records:
        policy, password = parse_record(record)
        if not (password and policy):
            continue
        num1, num2, character = parse_policy(policy)
        if not all((num1, num2, character)):
            continue
        if use_index:
            if validate_password_by_index(password, character, num1, num2):
                count += 1

        else:
            if validate_password_by_count(password, character, num1, num2):
                count += 1
    return count


def solve(filename):
    with open(filename) as f:
        lines = f.readlines()
    return count_valid_passwords(lines)


def solve2(filename):
    with open(filename) as f:
        lines = f.readlines()
    return count_valid_passwords(lines, use_index=True)


if __name__ == "__main__":
    solution = solve("data/day002.in")
    print("Day 002 (Part 1): ", solution)
    solution = solve2("data/day002.in")
    print("Day 002 (Part 2): ", solution)
