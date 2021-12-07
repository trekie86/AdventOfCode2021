def read_file_to_string_list(path: str) -> list[str]:
    input_lines = []
    with open(path) as f:
        for line in f:
            input_lines.append(str(line).strip())

    return input_lines


def read_file_to_int_list(path: str) -> list[int]:
    input_lines = []
    with open(path) as f:
        for line in f:
            input_lines.append(int(line))

    return input_lines


def read_line_single_line_to_ints(path: str) -> list[int]:
    with open(path) as f:
        return [int(i) for i in f.readline().split(',')]
