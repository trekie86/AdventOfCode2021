from util.fileutil import read_file_to_string_list
from util.list_util import split_lists_by_whitespace
from operator import itemgetter
import numpy as np


def process(step_count: int, print_output: bool = False):
    vals = read_file_to_string_list("data.txt")
    split_vals = split_lists_by_whitespace(vals)
    positions = [tuple(map(int, row.split(',', 1))) for row in split_vals[0]]
    fold_inst = split_vals[1]
    max_x = max(positions, key=itemgetter(0))[0]
    max_y = max(positions, key=itemgetter(1))[1]
    grid = np.zeros((max_y + 1, max_x + 1))
    for row in positions:
        grid[row[1], row[0]] = 1

    print(f"max values are {max_x} and {max_y}")
    if step_count == -1:
        step_count = len(fold_inst)
    for fold in fold_inst[:step_count]:
        fold_direction = fold.split()[2].split('=')[0]
        fold_index = int(fold.split()[2].split('=')[1])
        if fold_direction == 'y':
            new_grid = np.zeros((fold_index, grid.shape[1]))
            for step in range(1, fold_index + 1):
                for x in range(new_grid.shape[1]):
                    new_grid[fold_index - step, x] = grid[fold_index - step, x] + grid[fold_index + step, x]
            grid = new_grid
        else:
            new_grid = np.zeros((grid.shape[0], fold_index))
            for step in range(1, fold_index + 1):
                for y in range(new_grid.shape[0]):
                    new_grid[y, fold_index - step] = grid[y, fold_index - step] + grid[y, fold_index + step]
            grid = new_grid
        pretty_grid = np.where(grid > 0, '#', grid)
        pretty_grid = np.where(pretty_grid == '0.0', '.', pretty_grid)
        print(f"Current nonzeros after {fold} is {np.count_nonzero(grid)}")

    print(f"Shape is {grid.shape}")
    if print_output:
        for row in pretty_grid:
            print("".join(row))


def part1() -> None:
    process(1)


def part2() -> None:
    process(-1, True)


if __name__ == "__main__":
    part1()
    part2()
