import io

from .. import day006


def test_parse_groups_empty():
    data = ""
    groups = list(day006.parse_groups(io.StringIO(data)))

    assert len(groups) == 0


def test_parse_groups_single_group():
    data = """abc
    abcd
    ab"""

    groups = list(day006.parse_groups(io.StringIO(data)))

    assert groups == [["abc", "abcd", "ab"]]


def test_parse_groups_multiple_groups():
    data = """abc
    abcd
    ab

    a
    a
    a
    a

    ab
    cd"""

    groups = list(day006.parse_groups(io.StringIO(data)))

    assert len(groups) == 3
    assert len(groups[0]) == 3
    assert len(groups[1]) == 4
    assert len(groups[2]) == 2


def test_parse_groups_multiple_blanks():
    data = """abc
    abcd
    ab



    a
    a
    a
    a"""

    groups = list(day006.parse_groups(io.StringIO(data)))

    assert len(groups) == 2
    assert groups[0] == ["abc", "abcd", "ab"]
    assert groups[1] == ["a", "a", "a", "a"]


def test_count_answer_set_union_empty():
    answers = []
    count = day006.count_answer_set_union(answers)

    assert count == 0


def test_count_answer_set_union_single_entry():
    answers = ["abc"]
    count = day006.count_answer_set_union(answers)

    assert count == 3


def test_count_answer_set_union_matching_entries():
    answers = ["a", "a", "a", "a"]
    count = day006.count_answer_set_union(answers)

    assert count == 1


def test_count_answer_set_union_multiple_entries():
    answers = ["ab", "ac"]
    count = day006.count_answer_set_union(answers)

    assert count == 3


def test_count_answer_set_intersection_single_answer():
    answers = ["abc"]
    count = day006.count_answer_set_intersection(answers)

    assert count == 3


def test_count_answer_set_intersection_no_intersection():
    answers = ["abc", "def", "ghi"]
    count = day006.count_answer_set_intersection(answers)

    assert count == 0


def test_count_answer_set_intersection_single_intersection():
    answers = ["abc", "adef", "aghi"]
    count = day006.count_answer_set_intersection(answers)

    assert count == 1


def test_count_answer_set_intersection_all_intersect():
    answers = ["abc", "abc", "abc"]
    count = day006.count_answer_set_intersection(answers)

    assert count == 3


def test_part_one_exmaple():
    data = """abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b"""

    result = day006.part_one(io.StringIO(data))

    assert result == 11


def test_part_two_example():
    data = """abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b"""

    result = day006.part_two(io.StringIO(data))

    assert result == 6
