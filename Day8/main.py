from collections import defaultdict
from util.fileutil import read_file_to_string_list


class numberDisplay:
    def __init__(self, signal_wires: set[str]):
        self.signal_wires = signal_wires
        self.signal_count = len(signal_wires)


def string_to_char_set(word: str):
    return set([char for char in word])


def part1() -> None:
    number_map = get_number_map()
    # used for matching signal counts to potential numbers
    signal_count_to_number = defaultdict(list)
    for k, v in number_map.items():
        signal_count_to_number[v.signal_count].append(k)
    # used for measuring the output
    resulting_number_count = {i: 0 for i in range(10)}

    inputs, outputs = parse_inputs_outputs("data.txt")

    for output in outputs:
        nums = signal_count_to_number[len(output)]
        if len(nums) == 1:
            resulting_number_count[nums[0]] += 1

    result = resulting_number_count[1] + resulting_number_count[4] + resulting_number_count[7] \
        + resulting_number_count[8]
    print(f"The sum of 1, 4, 7, 8 occurrences is {result}")


def part2() -> None:
    number_map = get_number_map()

    # used for matching signal counts to potential numbers
    signal_count_to_number = defaultdict(list)
    for k, v in number_map.items():
        signal_count_to_number[v.signal_count].append(k)
    inputs, outputs = parse_inputs_outputs("data.txt")

    answers = []
    for (input_list, output_list) in zip(inputs, outputs):
        signal_mappings = {}
        mappings = {}
        inverse_mapping = {}
        length_to_input = defaultdict(set)
        for in_val in input_list:
            # Get all of the easy ones out of the way
            nums = signal_count_to_number[len(in_val)]
            # The easy case
            if len(nums) == 1:
                mappings[in_val] = nums[0]
                inverse_mapping[nums[0]] = in_val
            else:
                length_to_input[len(in_val)].add(in_val)

        # Now we can start using intersections to find out positional values
        signal_mappings['a'] = (set(inverse_mapping[7]) - set(inverse_mapping[1])).pop()

        # Now lets figure out the number 9. We can do this by looking at the inputs that are of length 6
        # and if we find the difference between 4 + the mapping of a, we now not only know the number 9
        # but the bottom signal mapping
        pseudo_val = set(inverse_mapping[4])
        pseudo_val.add(signal_mappings['a'])
        for val in length_to_input[6]:
            delta = set(val) - pseudo_val
            if len(delta) == 1:
                mappings[val] = 9
                inverse_mapping[9] = val
                signal_mappings['g'] = delta.pop()
                break
        # Now that we have 8 & 9, we know what the bottom left value 'e' actually is
        signal_mappings['e'] = (set(inverse_mapping[8]) - set(inverse_mapping[9])).pop()

        for val in length_to_input[6]:
            # We know we figured out 9, so filtering that out
            if val not in mappings:
                delta = set(inverse_mapping[8]) - set(val)
                if len(delta) == 1:
                    single_val = delta.pop()
                    # This means the only difference was c, so know we know c and we know that this is the number 6
                    if single_val in set(inverse_mapping[1]):
                        mappings[val] = 6
                        inverse_mapping[6] = val
                        signal_mappings['c'] = single_val
                        break
        for val in length_to_input[6]:
            # We already figured out 6 & 9, that just leaves 0
            if val not in mappings:
                mappings[val] = 0
                inverse_mapping[0] = val
                signal_mappings['d'] = (set(inverse_mapping[8]) - set(val)).pop()

        for val in length_to_input[5]:
            # Time to figure out 5
            pseudo_five = set(set(inverse_mapping[6]) - set(signal_mappings['e']))
            if set(val) == pseudo_five:
                mappings[val] = 5
                inverse_mapping[5] = val
            elif len(set(val) - set(inverse_mapping[7]) - set(signal_mappings['d']) - set(signal_mappings['g'])) == 0:
                # We figured out 3
                mappings[val] = 3
                inverse_mapping[3] = val

        for val in length_to_input[5]:
            if val not in mappings:
                mappings[val] = 2
                inverse_mapping[2] = val

        ans_str = ""
        for output in output_list:
            ans_str += str(mappings[output])
        answers.append(int(ans_str))

    print(f"The sum of the outputs is: {sum(answers)}")


def parse_inputs_outputs(path: str) -> ([], []):
    inputs = []
    outputs = []
    vals = read_file_to_string_list("data.txt")
    for row in vals:
        temp_input = []
        temp_output = []
        delim_reached = False
        for entry in row.split():
            if entry == '|':
                delim_reached = True
            elif delim_reached:
                temp_output.append("".join(sorted(entry)))
            else:
                temp_input.append("".join(sorted(entry)))
        inputs.append(temp_input)
        outputs.append(temp_output)
    return inputs, outputs


def get_number_map() -> {}:
    number_map = {
        0: numberDisplay(string_to_char_set('abcefg')),
        1: numberDisplay(string_to_char_set('cf')),
        2: numberDisplay(string_to_char_set('acdeg')),
        3: numberDisplay(string_to_char_set('acdfg')),
        4: numberDisplay(string_to_char_set('bcdf')),
        5: numberDisplay(string_to_char_set('abdfg')),
        6: numberDisplay(string_to_char_set('abdefg')),
        7: numberDisplay(string_to_char_set('acf')),
        8: numberDisplay(string_to_char_set('abcdefg')),
        9: numberDisplay(string_to_char_set('abcdfg'))
    }
    return number_map


if __name__ == "__main__":
    part1()
    part2()
