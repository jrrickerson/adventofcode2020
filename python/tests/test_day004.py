import io

from .. import day004


def test_parse_passport_empty():
    passport_string = ''
    expected_dict = {}

    passport = day004.parse_passport(passport_string)

    assert passport == expected_dict


def test_parse_passport_single_line():
    passport_string = (
        'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd '
        'byr:1937 iyr:2017 cid:147 hgt:183cm')
    expected_dict = {
        'ecl': 'gry',
        'pid': '860033327',
        'eyr': '2020',
        'hcl': '#fffffd',
        'byr': '1937',
        'iyr': '2017',
        'cid': '147',
        'hgt': '183cm'
    }
    passport = day004.parse_passport(passport_string)

    assert passport == expected_dict


def test_parse_passport_multi_line():
    passport_string = '''
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm'''
    expected_dict = {
        'ecl': 'gry',
        'pid': '860033327',
        'eyr': '2020',
        'hcl': '#fffffd',
        'byr': '1937',
        'iyr': '2017',
        'cid': '147',
        'hgt': '183cm'
    }
    passport = day004.parse_passport(passport_string)

    assert passport == expected_dict


def test_parse_passports_no_data():
    passport_data = ''
    expected_passports = 0
    passports = day004.parse_passports(io.StringIO(passport_data))

    assert len(passports) == expected_passports


def test_parse_passports_multi_blank_lines():
    passport_data = '''

        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm


        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929'''
    expected_passports = 2
    passports = day004.parse_passports(io.StringIO(passport_data))

    assert len(passports) == expected_passports


def test_parse_passports():
    passport_data = '''
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in'''
    expected_passports = 4
    passports = day004.parse_passports(io.StringIO(passport_data))

    assert len(passports) == expected_passports


def test_validate_passport_valid():
    passport = {
        'ecl': 'gry',
        'pid': '860033327',
        'eyr': '2020',
        'hcl': '#fffffd',
        'byr': '1937',
        'iyr': '2017',
        'cid': '147',
        'hgt': '183cm'
    }
    required_keys = ('ecl', 'pid', 'eyr', 'hcl')
    valid = day004.validate_passport(passport, required_keys)

    assert valid is True


def test_validate_passport_invalid():
    passport = {
        'ecl': 'gry',
        'pid': '860033327',
        'eyr': '2020',
        'hcl': '#fffffd',
        'byr': '1937',
        'iyr': '2017',
        'cid': '147',
        'hgt': '183cm'
    }
    required_keys = ('ecl', 'pid', 'eyr', 'hcl', 'abc')
    valid = day004.validate_passport(passport, required_keys)

    assert valid is False


def test_count_valid_passports_example():
    passport_data = '''
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in'''
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]

    # Pretend to be a file
    stream = io.StringIO(passport_data.strip())
    count = day004.count_valid_passports(stream, required_fields)

    assert count == 2
