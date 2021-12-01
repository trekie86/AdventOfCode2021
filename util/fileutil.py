def read_file_to_string_list(path: str) -> list[str]:
    input_lines = []
    with open(path) as f:
        for line in f:
            input_lines.append(str(line))

    return input_lines


def read_file_to_int_list(path: str) -> list[int]:
    input_lines = []
    with open(path) as f:
        for line in f:
            input_lines.append(int(line))

    return input_lines
