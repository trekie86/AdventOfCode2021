from util.fileutil import read_file_to_string_list
from util.list_util import split_lists_by_whitespace
from collections import Counter


def process(template: str, instructions: {}, steps: int) -> str:
    orig = template
    new_str = ""
    for step in range(1, steps + 1):
        print(f"Processing step {step}")
        range_length = len(orig) - 1
        for i in range(range_length):
            window = orig[i:i + 2]
            new_str += window[0]
            key = "".join(window)
            if key in instructions:
                new_str += instructions[key]
        new_str += orig[-1]
        orig = "".join(new_str)
        new_str = []
        # print(f"Current string {orig}")
    return orig


def process2(template: str, insructions: {}, steps: int) -> {}:
    counts = Counter()
    for i in range(len(template) - 1):
        key = "".join(template[i:i + 2])
        counts[key] += 1

    for step in range(1, steps + 1):
        new_counts = counts.copy()
        print(f"Processing step {step}")
        for key, value in counts.items():
            if value > 0:
                update = insructions[key]
                new_counts[f"{key[0]}{update}"] += value
                new_counts[f"{update}{key[1]}"] += value
                new_counts[key] -= value
        counts = new_counts

    return counts


def part1() -> None:
    vals = read_file_to_string_list("data.txt")
    parts = split_lists_by_whitespace(vals)
    template = parts[0][0]
    instructions = parts[1]
    instruction_map = {}
    for instruction in instructions:
        inst_parts = instruction.split(' -> ')
        instruction_map[inst_parts[0]] = inst_parts[1]
    result = process(template, instruction_map, 10)
    counter = Counter(result)
    sorted_results = sorted(counter.values(), reverse=True)
    print(f"Max {sorted_results[0]} minus min {sorted_results[-1]} is {sorted_results[0] - sorted_results[-1]}")


def part2() -> None:
    vals = read_file_to_string_list("data.txt")
    parts = split_lists_by_whitespace(vals)
    template = parts[0][0]
    instructions = parts[1]
    instruction_map = {}
    for instruction in instructions:
        inst_parts = instruction.split(' -> ')
        instruction_map[inst_parts[0]] = inst_parts[1]
    result = process2(template, instruction_map, 40)
    counter = Counter()
    for key, value in result.items():
        for char in key:
            counter[char] += value
    # We will be missing the first and last char so we need to add them back
    counter[template[0]] += 1
    counter[template[-1]] += 1
    # We've counted twice as many so time to divide
    for key in counter:
        counter[key] //= 2

    sorted_results = sorted(counter.values(), reverse=True)
    print(f"Max {sorted_results[0]} minus min {sorted_results[-1]} is {sorted_results[0] - sorted_results[-1]}")


if __name__ == "__main__":
    part1()
    part2()
