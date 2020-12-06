'''Advent of Code 2020
   Day 4 Solution - Passport Processing
'''


def parse_passports(data):
    passports = []
    passport_string = ''
    for line in data:
        line = line.lstrip()
        if not line and passport_string:
            try:
                passport = parse_passport(passport_string)
                passports.append(passport)
            except ValueError:
                print('Could not parse ', passport_string)
            passport_string = ''
        else:
            passport_string += line
    if passport_string:
        try:
            passport = parse_passport(passport_string)
            passports.append(passport)
        except ValueError:
            print('Could not parse ', passport_string)
    return passports


def parse_passport(passport_string):
    return dict([
        pair.split(':') for pair in passport_string.split()])


def validate_passport(passport, required_keys):
    return set(required_keys) <= set(passport.keys())


def count_valid_passports(data, required_fields=None):
    required_fields = required_fields or None
    valid_passports = 0
    passports = parse_passports(data)
    for passport in passports:
        valid = validate_passport(passport, required_fields)
        if valid:
            valid_passports += 1

    return valid_passports


def solve(filename):
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]

    with open(filename) as f:
        count = count_valid_passports(
            f, required_fields=required_fields)

    return count


if __name__ == '__main__':
    solution = solve('data/day004.in')
    print('Day 004 (Part 1): ', solution)

