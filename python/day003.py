'''Advent of Code 2020
   Day 2 Solution - Tobaggan Trajectory
'''
from collections import namedtuple

Vector = namedtuple('Vector', ['x', 'y'])


def generate_grid(grid_data):
    '''Given a multi-line string of text containing symbols, generate a
    two-dimensional list of values.
    Symbol Map:
        . = 0
        # = 1'''
    if not grid_data:
        return []
    grid = [
        [1 if char == '#' else 0 for char in line]
        for line in grid_data.strip().split()]
    return grid


def next_pos(pos, grid_size, trajectory):
    '''Given a position, grid size, and trajectory vector, calculate
    the next position along the trajectory within the grid given PacMan style
    wraparound rules'''
    newpos = Vector(
        x=(pos.x + trajectory.x) % grid_size.x,
        y=(pos.y + trajectory.y) % grid_size.y)
    return newpos


def count_trees(grid_data, trajectory, start=Vector(0, 0)):
    '''Using a textual representation of a grid, navigate the grid using a
    start position and trajectory and count the number of "trees"
    encountered.'''
    if not (grid_data and trajectory):
        raise ValueError('Empty grid or trajectory specified')
    grid = generate_grid(grid_data)
    grid_size = Vector(len(grid[0]), len(grid))
    print('Grid Size', grid_size)
    tree_count = 0
    pos = start
    while True:
        print('Position', pos)
        pos = next_pos(pos, grid_size, trajectory)
        tree_count += grid[pos.y][pos.x]
        if pos.y == grid_size.y - 1:
            break
    return tree_count


def solve(filename):
    with open(filename) as f:
        grid_data = f.read()
    trajectory = Vector(3, 1)
    return count_trees(grid_data, trajectory)


if __name__ == '__main__':
    solution = solve('data/day003.in')
    print('Day 003 (Part 1): ', solution)
