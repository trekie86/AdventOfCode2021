from util.fileutil import read_file_to_string_list, read_file_to_int_list
import re


def part1() -> None:
    raw_vals = read_file_to_string_list("data.txt")[0]
    x_min, x_max, y_min, y_max = map(int, re.findall(r"[-\d]+", raw_vals))
    print(f"x_min: {x_min}, x_max: {x_max}, y_min: {y_min}, y_max: {y_max}")

    # Since the Y value always goes down by one per step that means that the steps are summed as n(n+1)/2
    # and since what goes up must come down, we can just calculate the max height using the min y value

    print(f"Max y is {(abs(y_min) * abs(y_min + 1)) // 2}")


def simulate(star_x: int, start_y: int, x_min: int, x_max: int, y_min: int, y_max: int) -> bool:
    cur_x = star_x
    xs = [cur_x]
    max_x = 0
    while xs[-1] < x_max or cur_x != 0:
        if cur_x == 0:
            max_x = xs[-1]
            break
        cur_x += 1 if cur_x < 0 else -1
        xs.append(cur_x + xs[-1])

    max_steps = -1
    min_steps = -1
    for idx, val in enumerate(xs):
        if x_min <= val <= x_max:
            if min_steps == -1:
                min_steps = idx
                max_steps = idx
            else:
                max_steps = idx
        elif val > x_max:
            break

    if min_steps == -1:
        return False
    cur_y = start_y
    y_val = 0
    step = 0
    while True:
        y_val += cur_y
        cur_y -= 1
        if y_min <= y_val <= y_max and (min_steps <= step <= max_steps or (step > max_steps and max_x != 0)):
            return True
        step += 1
        if y_val < y_min:
            return False


def part2() -> None:
    raw_vals = read_file_to_string_list("data.txt")[0]
    x_min, x_max, y_min, y_max = map(int, re.findall(r"[-\d]+", raw_vals))
    updated_y_max = max(abs(y_min), abs(y_max))
    success = 0
    for x in range(x_max + 1):
        for y in range(-updated_y_max, updated_y_max + 1):
            print(f"Testing x: {x}, y: {y}...result: ", end="")
            result = simulate(x, y, x_min, x_max, y_min, y_max)
            success += 1 if result is True else 0
            print(result)
    print(f"Total successful options are {success}")


if __name__ == "__main__":
    part1()
    part2()
