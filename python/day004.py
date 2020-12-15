"""Advent of Code 2020
   Day 4 Solution - Passport Processing
"""
import re

RE_VALID_HAIR_COLOR = "^#[0-9a-f]{6}$"
RE_VALID_PID = "^[0-9]{9}$"


def validate_height(value):
    return (value.endswith("cm") and (150 <= int(value[:-2]) <= 193)) or (
        value.endswith("in") and (59 <= int(value[:-2]) <= 76)
    )


def parse_passports(data):
    passports = []
    passport_string = ""
    for line in data:
        line = line.lstrip()
        if not line and passport_string:
            try:
                passport = parse_passport(passport_string)
                passports.append(passport)
            except ValueError:
                print("Could not parse ", passport_string)
            passport_string = ""
        else:
            passport_string += line
    if passport_string:
        try:
            passport = parse_passport(passport_string)
            passports.append(passport)
        except ValueError:
            print("Could not parse ", passport_string)
    return passports


def parse_passport(passport_string):
    return dict([pair.split(":") for pair in passport_string.split()])


def validate_passport(passport, required_keys, validation_rules={}):
    if not set(required_keys) <= set(passport.keys()):
        return False
    for key, rule in validation_rules.items():
        if not rule(passport.get(key)):
            return False
        # print(passport.get(key), 'valid for', key)
    return True


def count_valid_passports(data, required_fields=None, validation_rules={}):
    required_fields = required_fields or None
    valid_passports = 0
    passports = parse_passports(data)
    for passport in passports:
        valid = validate_passport(passport, required_fields, validation_rules)
        if valid:
            valid_passports += 1

    return valid_passports


def solve(filename):
    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]

    with open(filename) as f:
        count = count_valid_passports(f, required_fields=required_fields)

    return count


def solve2(filename):
    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
    validation_rules = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hgt": validate_height,
        "hcl": lambda x: re.match(RE_VALID_HAIR_COLOR, x),
        "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda x: re.match(RE_VALID_PID, x),
    }

    with open(filename) as f:
        count = count_valid_passports(
            f, required_fields=required_fields, validation_rules=validation_rules
        )

    return count


if __name__ == "__main__":
    solution = solve("data/day004.in")
    print("Day 004 (Part 1): ", solution)
    solution = solve2("data/day004.in")
    print("Day 004 (Part 2): ", solution)
