from .. import day002


def test_parse_record_empty_string():
    record = ''
    policy, password = day002.parse_record(record)

    assert policy == ''
    assert password == ''


def test_parse_record_no_separator():
    record = '1-10 z'
    policy, password = day002.parse_record(record)

    assert policy == ''
    assert password == ''


def test_parse_record_no_password():
    record = '1-10 z: '
    policy, password = day002.parse_record(record)

    assert policy == '1-10 z'
    assert password == ''


def test_parse_record_no_policy():
    record = ': mypass'
    policy, password = day002.parse_record(record)

    assert policy == ''
    assert password == 'mypass'


def test_parse_record_ignore_whitespace():
    record = '   1-10 z: zzzzz    '
    policy, password = day002.parse_record(record)

    assert policy == '1-10 z'
    assert password == 'zzzzz'


def test_parse_policy_empty():
    policy = ''
    lower, upper, character = day002.parse_policy(policy)

    assert lower == 0
    assert upper == 0
    assert character == ''


def test_parse_policy_no_separator():
    policy = '1-10z'
    lower, upper, character = day002.parse_policy(policy)

    assert lower == 0
    assert upper == 0
    assert character == ''


def test_parse_policy_no_character():
    policy = '1-10 '
    lower, upper, character = day002.parse_policy(policy)

    assert lower == 0
    assert upper == 0
    assert character == ''


def test_parse_policy_no_range():
    policy = ' z'
    lower, upper, character = day002.parse_policy(policy)

    assert lower == 0
    assert upper == 0
    assert character == ''


def test_parse_policy_range_invalid():
    policy = '10 z'
    lower, upper, character = day002.parse_policy(policy)

    assert lower == 0
    assert upper == 0
    assert character == ''


def test_parse_policy_valid():
    policy = '1-10 z'
    lower, upper, character = day002.parse_policy(policy)

    assert lower == 1
    assert upper == 10
    assert character == 'z'


def test_count_valid_passwords_empty():
    password_entries = []
    valid = day002.count_valid_passwords(password_entries)

    assert valid == 0


def test_count_valid_passwords_example():
    password_entries = [
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc'
    ]

    valid = day002.count_valid_passwords(password_entries)

    assert valid == 2
