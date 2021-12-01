from util.fileutil import read_file_to_int_list


def part1() -> None:
    vals: list[int] = read_file_to_int_list("input.txt")
    increments: int = 0
    for i in range(1, len(vals)):
        if vals[i - 1] < vals[i]:
            increments += 1
    print(f"There are {increments} increment values")


def part2() -> None:
    vals: list[int] = read_file_to_int_list("input.txt")
    increments: int = 0
    for i in range(1, len(vals)-2):
        prev_window: int = vals[i-1] + vals[i] + vals[i+1]
        next_window: int = vals[i] + vals[i + 1] + vals[i + 2]
        if prev_window < next_window:
            increments += 1
    print(f"There are {increments} increment values with windows")


if __name__ == '__main__':
    part1()
    part2()
