import io
import re

from .. import day004


def test_parse_passport_empty():
    passport_string = ""
    expected_dict = {}

    passport = day004.parse_passport(passport_string)

    assert passport == expected_dict


def test_parse_passport_single_line():
    passport_string = (
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd "
        "byr:1937 iyr:2017 cid:147 hgt:183cm"
    )
    expected_dict = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    passport = day004.parse_passport(passport_string)

    assert passport == expected_dict


def test_parse_passport_multi_line():
    passport_string = """
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm"""
    expected_dict = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    passport = day004.parse_passport(passport_string)

    assert passport == expected_dict


def test_parse_passports_no_data():
    passport_data = ""
    expected_passports = 0
    passports = day004.parse_passports(io.StringIO(passport_data))

    assert len(passports) == expected_passports


def test_parse_passports_multi_blank_lines():
    passport_data = """

        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm


        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929"""
    expected_passports = 2
    passports = day004.parse_passports(io.StringIO(passport_data))

    assert len(passports) == expected_passports


def test_parse_passports():
    passport_data = """
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in"""
    expected_passports = 4
    passports = day004.parse_passports(io.StringIO(passport_data))

    assert len(passports) == expected_passports


def test_validate_passport_valid():
    passport = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    required_keys = ("ecl", "pid", "eyr", "hcl")
    valid = day004.validate_passport(passport, required_keys)

    assert valid is True


def test_validate_passport_invalid():
    passport = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    required_keys = ("ecl", "pid", "eyr", "hcl", "abc")
    valid = day004.validate_passport(passport, required_keys)

    assert valid is False


def test_validate_passport_empty_validation():
    passport = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    required_keys = ("ecl", "pid", "eyr", "hcl")
    valid = day004.validate_passport(passport, required_keys, validation_rules={})

    assert valid is True


def test_validate_passport_validation_rules():
    passport = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    required_keys = ("ecl", "pid", "eyr", "hcl")
    validation_rules = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "hcl": lambda x: re.match("#[0-9a-f]{6}", x),
    }
    valid = day004.validate_passport(
        passport, required_keys, validation_rules=validation_rules
    )

    assert valid is True


def test_validate_passport_validation_rules_invalid():
    passport = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    required_keys = ("ecl", "pid", "eyr", "hcl")
    validation_rules = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "hcl": lambda x: re.match("#[0-9a-f]{6}", x),
        "ecl": lambda x: x in ("abc", "def"),
    }
    valid = day004.validate_passport(
        passport, required_keys, validation_rules=validation_rules
    )

    assert valid is False


def test_validate_height_no_units():
    value = "136"
    valid = day004.validate_height(value)

    assert valid is False


def test_validate_height_out_of_range():
    value = "72cm"
    valid = day004.validate_height(value)

    assert valid is False


def test_validate_height_inches():
    value = "72in"
    valid = day004.validate_height(value)

    assert valid is True


def test_validate_height_centimeters():
    value = "155cm"
    valid = day004.validate_height(value)

    assert valid is True


def test_count_valid_passports_example():
    passport_data = """
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in"""
    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]

    # Pretend to be a file
    stream = io.StringIO(passport_data.strip())
    count = day004.count_valid_passports(stream, required_fields)

    assert count == 2


def test_count_valid_passports_example_part2_invalid():
    passport_data = """
        eyr:1972 cid:100
        hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

        iyr:2019
        hcl:#602927 eyr:1967 hgt:170cm
        ecl:grn pid:012533040 byr:1946

        hcl:dab227 iyr:2012
        ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

        hgt:59cm ecl:zzz
        eyr:2038 hcl:74454a iyr:2023
        pid:3556412378 byr:2007"""
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validation_rules = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hgt": day004.validate_height,
        "hcl": lambda x: re.match(day004.RE_VALID_HAIR_COLOR, x),
        "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda x: re.match(day004.RE_VALID_PID, x),
    }

    # Pretend to be a file
    stream = io.StringIO(passport_data.strip())
    count = day004.count_valid_passports(stream, required_fields, validation_rules)

    assert count == 0


def test_count_valid_passports_example_part2_valid():
    passport_data = """
        pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
        hcl:#623a2f

        eyr:2029 ecl:blu cid:129 byr:1989
        iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

        hcl:#888785
        hgt:164cm byr:2001 iyr:2015 cid:88
        pid:545766238 ecl:hzl
        eyr:2022

        iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
        """
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    validation_rules = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hgt": day004.validate_height,
        "hcl": lambda x: re.match(day004.RE_VALID_HAIR_COLOR, x),
        "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda x: re.match(day004.RE_VALID_PID, x),
    }

    # Pretend to be a file
    stream = io.StringIO(passport_data.strip())
    count = day004.count_valid_passports(stream, required_fields, validation_rules)

    assert count == 4
