import io

from .. import day005


def test_binary_partition_all_zeros_equals_zero():
    '''Test the sequence of all 0s results in the lowest value in the range'''
    sequence = [0, 0, 0, 0, 0, 0, 0]
    max_range = 128

    value = day005.binary_partition(sequence, max_range)

    assert value == 0


def test_binary_partition_all_ones_equals_max_range_minus_one():
    '''Test the sequence of all 1s results in the highest value in the range'''
    sequence = [1, 1, 1, 1, 1, 1, 1]
    max_range = 128

    value = day005.binary_partition(sequence, max_range)

    assert value == 127


def test_binary_partition_sequence_exceeds_max_range():
    '''Test that the sequence supplying too many values does not affect
    the value'''
    # All values after the 7th should be ignored
    sequence = [0, 0, 1, 0, 0, 1, 0, 1, 1]
    max_range = 128

    value = day005.binary_partition(sequence, max_range)

    assert value == 18


def test_binary_partition_sequence_example_rows():
    '''Test the binary sequence example provided by the problem statement'''
    # FBFBBFF
    sequence = [0, 1, 0, 1, 1, 0, 0]
    max_range = 128

    value = day005.binary_partition(sequence, max_range)

    assert value == 44


def test_binary_partition_sequence_example_cols():
    '''Test the binary sequence example provided by the problem statement'''
    # RLR
    sequence = [1, 0, 1]
    max_range = 8

    value = day005.binary_partition(sequence, max_range)

    assert value == 5


def test_to_binary_sequence_empty():
    '''Test conversion to a binary sequence for an empty string'''
    in_string = ''

    sequence = day005.to_binary_sequence(in_string, onchars='F')

    assert len(sequence) == 0


def test_to_binary_sequence_no_onchars_all_zeros():
    '''Test conversion to a binary sequence for an empty string'''
    in_string = 'ABCDEFG'

    sequence = day005.to_binary_sequence(in_string)

    assert len(sequence) == len(in_string)
    assert all([0 == i for i in sequence])


def test_to_binary_sequence_all_onchars():
    '''Test conversion to a binary sequence for an empty string'''
    in_string = 'ABCDEFG'

    sequence = day005.to_binary_sequence(in_string, onchars='ABCDEFG')

    assert len(sequence) == len(in_string)
    assert all([1 == i for i in sequence])


def test_to_binary_sequence_two_characters():
    '''Test conversion to a binary sequence for an empty string'''
    in_string = 'FFBBFBF'

    sequence = day005.to_binary_sequence(in_string, onchars='B')

    assert len(sequence) == len(in_string)
    assert sequence == [0, 0, 1, 1, 0, 1, 0]


def test_to_binary_sequence_many_off_chars():
    '''Test conversion to a binary sequence for an empty string'''
    in_string = 'OOAQOBOXXY'

    sequence = day005.to_binary_sequence(in_string, onchars='O')

    assert len(sequence) == len(in_string)
    assert sequence == [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]


def test_part_one_examples():
    data = 'FBFBBFFRLR'
    seat_id = day005.part_one(io.StringIO(data), rows=128, cols=8)

    assert seat_id == 357

    data = 'BFFFBBFRRR'
    seat_id = day005.part_one(io.StringIO(data), rows=128, cols=8)

    assert seat_id == 567

    data = 'FFFBBBFRRR'
    seat_id = day005.part_one(io.StringIO(data), rows=128, cols=8)

    assert seat_id == 119

    data = 'BBFFBBFRLL'
    seat_id = day005.part_one(io.StringIO(data), rows=128, cols=8)

    assert seat_id == 820
