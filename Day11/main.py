from util.fileutil import read_file_to_string_list
import numpy as np

max_idx = 9


def part1() -> None:
    vals = read_file_to_string_list("sample.txt")
    raw_data = []

    steps = 100
    for row in vals:
        raw_data.append([int(i) for i in row])
    grid = np.array(raw_data)
    flashes = 0
    for step in range(1, steps + 1):
        print(f"Processing step {step}, flashes currently at {flashes}")
        grid += 1
        # Do the flashing stuff here
        while np.count_nonzero(grid == 10):
            for (y, x) in np.transpose(np.nonzero(grid == 10)):
                flashes += 1
                flash((y, x), grid, flashes)
                # Setting it a big number so we don't count it again
                grid[y, x] = 100
        grid = np.where(grid > 9, 0, grid)

    print(f"The total number was flashes after {steps} steps was {flashes}")


def part2() -> None:
    vals = read_file_to_string_list("data.txt")
    raw_data = []

    for row in vals:
        raw_data.append([int(i) for i in row])
    grid = np.array(raw_data)
    flashes = 0
    step = 1
    while True:
        last_step_flashes = flashes
        print(f"Processing step {step}, flashes currently at {flashes}")
        grid += 1
        # Do the flashing stuff here
        while np.count_nonzero(grid == 10):
            for (y, x) in np.transpose(np.nonzero(grid == 10)):
                flashes += 1
                flash((y, x), grid, flashes)
                # Setting it a big number so we don't count it again
                grid[y, x] = 100
        grid = np.where(grid > 9, 0, grid)
        if flashes - last_step_flashes == 100:
            print(f"They all flash at step {step}")
            return
        step += 1


def flash(pos: (int, int), grid: [], flashes: int) -> None:
    # Increment all of the neighbors but ensure you don't overwrite a 10 that is supposed to flash
    y, x = pos
    if y > 0 and x > 0 and grid[y - 1, x - 1] < 10:
        grid[y - 1, x - 1] += 1
    if y > 0 and grid[y - 1, x] < 10:
        grid[y - 1, x] += 1
    if x > 0 and grid[y, x - 1] < 10:
        grid[y, x - 1] += 1
    if y < max_idx and x < max_idx and grid[y + 1, x + 1] < 10:
        grid[y + 1, x + 1] += 1
    if y < max_idx and grid[y + 1, x] < 10:
        grid[y + 1, x] += 1
    if x < max_idx and grid[y, x + 1] < 10:
        grid[y, x + 1] += 1
    if y > 0 and x < max_idx and grid[y - 1, x + 1] < 10:
        grid[y - 1, x + 1] += 1
    if y < max_idx and x > 0 and grid[y + 1, x - 1] < 10:
        grid[y + 1, x - 1] += 1


if __name__ == "__main__":
    part1()
    part2()
