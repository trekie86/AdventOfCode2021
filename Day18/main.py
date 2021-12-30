import itertools

from util.fileutil import read_file_to_string_list
import re
import math

DEBUG = False


def validate_format(in_str: str) -> None:
    depth = 0
    for char in in_str:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1

    if depth != 0:
        raise ValueError(f"The brackets for {in_str} do not match")


def add_strings(first_str: str, second_str: str) -> str:
    process_str = f"[{first_str},{second_str}]"
    if DEBUG:
        print(f"Starting point: {process_str}")
    finished = False
    done_exploding = False
    while not finished:
        current_pair_depth = 0
        most_recent_left_val = None
        most_recent_left_val_idx = None
        for cur_idx, char in enumerate(process_str):
            if char == ',':
                continue
            elif char == '[':
                current_pair_depth += 1
                continue
            elif char == ']':
                current_pair_depth -= 1
                if current_pair_depth == 0:
                    if done_exploding:
                        finished = True
                    else:
                        done_exploding = True
                    break
                continue
            elif current_pair_depth == 5:
                # Do the explode stuff
                pair_left_idx = cur_idx - 1
                pair_right_idx = process_str.index(']', pair_left_idx)
                exploding_pair_str = process_str[pair_left_idx:pair_right_idx + 1]
                res = re.finditer(r'\d+', process_str[cur_idx:])
                left_val = int(next(res).group())
                right_val = int(next(res).group())
                next_match = next(res, None)
                # Replace the newly added right value, need to consider the correct position
                if next_match is not None:
                    next_match_val = int(next_match.group())
                    new_right_val = right_val + next_match_val
                    process_str = f"{process_str[:next_match.start() + cur_idx]}{new_right_val}{process_str[next_match.end() + cur_idx:]}"
                    if DEBUG:
                        validate_format(process_str)

                # Replace the exploding pair with a 0
                process_str = f"{process_str[:pair_left_idx]}0{process_str[pair_right_idx + 1:]}"
                if DEBUG:
                    validate_format(process_str)
                # Update the left regular value if it was present
                if most_recent_left_val is not None:
                    # This means there was an earlier number and we need to actually replace the value with the sum
                    new_left_val = left_val + most_recent_left_val
                    # Replace the most recent left value with the new one but it may shift the string if it is > 9,
                    process_str = f"{process_str[:most_recent_left_val_idx]}{new_left_val}{process_str[most_recent_left_val_idx + len(str(most_recent_left_val)):]}"
                    if DEBUG:
                        validate_format(process_str)
                # Stop this run and start over again
                if DEBUG:
                    print(f"After explode:\t{process_str}")
                break
            else:
                res = re.finditer(r'\d+', process_str[cur_idx:])
                match = next(res)
                cur_val = int(match.group())
                if cur_val >= 10 and done_exploding:
                    # do split stuff
                    new_str = f"[{int(math.floor(cur_val / 2))},{int(math.ceil(cur_val / 2))}]"
                    # Rebuild the string
                    process_str = f"{process_str[:match.start() + cur_idx]}{new_str}{process_str[match.end() + cur_idx:]}"
                    # Due to the split, there may be an explode that needs to happen. Reset the flag and start again
                    done_exploding = False
                    if DEBUG:
                        validate_format(process_str)
                        print(f"After split:\t{process_str}")
                    break
                else:
                    if most_recent_left_val and most_recent_left_val > 10 and most_recent_left_val_idx == cur_idx - 1:
                        continue
                    most_recent_left_val = cur_val
                    most_recent_left_val_idx = cur_idx
                    continue
    return process_str


def calculate_magnitude(in_str: str) -> int:
    # Basically iterate to find pairs until there is only one pair left
    while in_str.count(",") > 1:
        for p in re.findall("\[\d+,\d+\]", in_str):
            pair = re.search(re.escape(p), in_str)
            left_digit, right_digit = p[1:-1].split(",")
            in_str = f"{in_str[: pair.start()]}{int(left_digit) * 3 + int(right_digit) * 2}{in_str[pair.end():]}"
    left_digit, right_digit = in_str[1:-1].split(",")
    return int(left_digit) * 3 + int(right_digit) * 2


def part1() -> None:
    raw_vals = read_file_to_string_list("data.txt")
    first_str = raw_vals[0]
    for next_val in raw_vals[1:]:
        first_str = add_strings(first_str, next_val)

    print(f"Calculating magnitude for {first_str}")
    magnitude = calculate_magnitude(first_str)
    print(f"The magnitude of the final sum is {magnitude}")


def part2() -> None:
    raw_vals = read_file_to_string_list("data.txt")
    permutations = itertools.permutations(raw_vals, 2)
    results = []
    for permu in permutations:
        result = add_strings(permu[0], permu[1])
        mag = calculate_magnitude(result)
        results.append(mag)

    print(f"The largest magnitude of two pairs is {max(results)}")


if __name__ == "__main__":
    DEBUG = False
    part1()
    part2()
