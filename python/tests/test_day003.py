import functools
import operator
import pytest
from pprint import pprint
from .. import day003


def test_generate_grid_empty():
    '''Test that an empty grid string produces and empty grid'''
    grid_data = ''
    grid = day003.generate_grid(grid_data)

    assert grid == []


def test_generate_grid_matches_dimensions():
    '''Test that the grid generated matches the dimensions of the
    string data'''
    grid_data = '''
        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#'''

    expected_rows = grid_data.strip().count('\n') + 1
    expected_columns = grid_data.strip().index('\n')
    grid = day003.generate_grid(grid_data)

    pprint(grid)
    assert len(grid) == expected_rows
    assert len(grid[0]) == expected_columns


def test_next_pos_positive_x_trajectory():
    start = day003.Vector(0, 0)
    grid_size = day003.Vector(20, 20)
    trajectory = day003.Vector(3, 1)

    expected_pos = day003.Vector(3, 1)
    pos = day003.next_pos(start, grid_size, trajectory)

    assert pos == expected_pos


def test_next_pos_negative_x_trajectory():
    start = day003.Vector(5, 5)
    grid_size = day003.Vector(20, 20)
    trajectory = day003.Vector(-3, 1)

    expected_pos = day003.Vector(2, 6)
    pos = day003.next_pos(start, grid_size, trajectory)

    assert pos == expected_pos


def test_next_pos_negative_y_trajectory():
    start = day003.Vector(5, 5)
    grid_size = day003.Vector(20, 20)
    trajectory = day003.Vector(3, -1)

    expected_pos = day003.Vector(8, 4)
    pos = day003.next_pos(start, grid_size, trajectory)

    assert pos == expected_pos


def test_next_pos_x_wraparound():
    start = day003.Vector(19, 5)
    grid_size = day003.Vector(20, 20)
    trajectory = day003.Vector(3, 1)

    expected_pos = day003.Vector(2, 6)
    pos = day003.next_pos(start, grid_size, trajectory)

    assert pos == expected_pos


def test_next_pos_y_wraparound():
    start = day003.Vector(5, 19)
    grid_size = day003.Vector(20, 20)
    trajectory = day003.Vector(3, 1)

    expected_pos = day003.Vector(8, 0)
    pos = day003.next_pos(start, grid_size, trajectory)

    assert pos == expected_pos


def test_next_pos_negative_x_wraparound():
    start = day003.Vector(0, 5)
    grid_size = day003.Vector(20, 20)
    trajectory = day003.Vector(-3, 1)

    expected_pos = day003.Vector(17, 6)
    pos = day003.next_pos(start, grid_size, trajectory)

    assert pos == expected_pos


def test_next_pos_negative_y_wraparound():
    start = day003.Vector(0, 0)
    grid_size = day003.Vector(20, 20)
    trajectory = day003.Vector(3, -1)

    expected_pos = day003.Vector(3, 19)
    pos = day003.next_pos(start, grid_size, trajectory)

    assert pos == expected_pos


def test_count_trees_empty_grid_raises():
    '''Test that an empty grid raises an exception'''
    grid_data = ''
    trajectory = (1, 1)

    with pytest.raises(ValueError):
        day003.count_trees(grid_data, trajectory)


def test_count_trees_empty_trajectory_raises():
    grid_data = '''
        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#'''
    trajectory = ()

    with pytest.raises(ValueError):
        day003.count_trees(grid_data, trajectory)


def test_count_trees_example():
    grid_data = '''
        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#'''
    trajectory = day003.Vector(3, 1)

    trees = day003.count_trees(grid_data, trajectory)

    assert trees == 7


def test_count_trees_example_part2():
    grid_data = '''
        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#'''

    trajectories = [
        day003.Vector(1, 1),
        day003.Vector(3, 1),
        day003.Vector(5, 1),
        day003.Vector(7, 1),
        day003.Vector(1, 2),
    ]

    tree_counts = [
        day003.count_trees(grid_data, trajectory)
        for trajectory in trajectories]
    product = functools.reduce(operator.mul, tree_counts)

    assert product == 336
