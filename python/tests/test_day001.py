'''Unit tests for Day 1 solution to Advent of Code 2020'''
from .. import day001


def test_build_index_empty():
    index = day001.build_index('')
    assert index == {}


def test_build_index_single_line():
    inputstr = '1234'
    index = day001.build_index(inputstr)
    assert len(index) == 1
    assert index.get('1234') is not None


def test_build_index_multi_line():
    inputstr = '''
        1234
        5678'''
    index = day001.build_index(inputstr)
    assert len(index) == 2
    assert index.get('1234') is not None
    assert index.get('5678') is not None


def test_build_index_ignores_whitespace():
    inputstr = '''
             1234

        5678   '''
    index = day001.build_index(inputstr)
    assert len(index) == 2
    assert index.get('1234') is not None
    assert index.get('5678') is not None


def test_build_index_line_numbers():
    inputstr = '''
    1234
    5678
    1111
    2222
    3333'''
    index = day001.build_index(inputstr)
    assert len(index) == 5
    assert index.get('1234') == 0
    assert index.get('5678') == 1
    assert index.get('3333') == 4


def test_build_index_transform_values():
    inputstr = '''
    1234
    5678
    1111
    2222
    3333'''
    index = day001.build_index(inputstr, transform=int)
    assert len(index) == 5
    assert all([type(value) == int for value in index.keys()])


def test_find_factors_empty_index():
    index = {}
    target = 1000
    f1, f2 = day001.find_factors(index, target)

    assert f1 == 0
    assert f2 == 0


def test_find_factors_not_found():
    index = {
        10: 0,
        11: 1
    }
    target = 1000
    f1, f2 = day001.find_factors(index, target)

    assert f1 == 0
    assert f2 == 0


def test_find_factors_correct_sum():
    index = {value: i for i, value in enumerate(range(100, 200))}
    target = 300

    f1, f2 = day001.find_factors(index, target)

    assert f1 + f2 != 0
    assert f1 + f2 == target
