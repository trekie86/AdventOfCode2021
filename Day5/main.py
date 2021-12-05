from util.fileutil import read_file_to_string_list
import numpy as np


def part1() -> None:
    raw_vals = read_file_to_string_list("data.txt")
    from_pairs = []
    to_pairs = []
    for row in raw_vals:
        from_pair, to_pair = row.split(' -> ')
        from_pairs.append([int(i) for i in from_pair.split(',')])
        to_pairs.append([int(i) for i in to_pair.split(',')])

    max_val = max(np.max(from_pairs), np.max(to_pairs))
    np_array = np.zeros((max_val + 1, max_val + 1))

    for (x1, y1), (x2, y2) in zip(from_pairs, to_pairs):
        # print(np_array)
        # print()
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                np_array[y, x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                np_array[y1, x] += 1

    print(np_array)
    print(np.count_nonzero(np_array > 1))


def part2() -> None:
    raw_vals = read_file_to_string_list("data.txt")
    from_pairs = []
    to_pairs = []
    for row in raw_vals:
        from_pair, to_pair = row.split(' -> ')
        from_pairs.append([int(i) for i in from_pair.split(',')])
        to_pairs.append([int(i) for i in to_pair.split(',')])

    max_val = max(np.max(from_pairs), np.max(to_pairs))
    np_array = np.zeros((max_val + 1, max_val + 1))

    for (x1, y1), (x2, y2) in zip(from_pairs, to_pairs):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                np_array[y, x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                np_array[y1, x] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            x_slope, y_slope = 1, 1
            if x1 > x2:
                x_slope = -1
            if y1 > y2:
                y_slope = -1
            for delta in range(abs(x1 - x2) + 1):
                np_array[y1 + delta * y_slope, x1 + delta * x_slope] += 1

    print(np_array)
    print(np.count_nonzero(np_array > 1))


if __name__ == "__main__":
    part1()
    part2()
