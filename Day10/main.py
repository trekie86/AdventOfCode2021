from util.fileutil import read_file_to_string_list
from queue import LifoQueue


def part1() -> None:
    illegal_char_val = {')': 3, ']': 57, '}': 1197, '>': 25137}
    illegal_chars = []
    vals = read_file_to_string_list("data.txt")
    for row in vals:
        process_row(row, illegal_chars)

    total = 0
    for char in illegal_chars:
        total += illegal_char_val[char]
    print(f"The illegal chars value is {total}")


def process_row(row: [], illegal_chars: []) -> list[str]:
    stack = LifoQueue()
    symbols = [char for char in row]
    closing_symbols = ""
    for symbol in symbols:
        if is_open(symbol):
            stack.put(symbol)
        else:
            if not is_matching_braces(stack.get(), symbol):
                illegal_chars.append(symbol)
                return []
    while not stack.empty():
        closing_symbols += get_matching_brace(stack.get())
    return closing_symbols


def part2() -> None:
    vals = read_file_to_string_list("data.txt")
    # I don't really need this but I don't want to duplicate code
    illegal_chars = []
    closing_symbols = []
    for row in vals:
        closing_symbols.append(process_row(row, illegal_chars))

    close_symbol_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    # calculate scores
    for symbols in closing_symbols:
        score = 0
        for char in symbols:
            score *= 5
            score += close_symbol_scores[char]
        if score != 0:
            scores.append(score)
    scores.sort()
    result = scores[len(scores) // 2]
    print(f"The middle corrective score is {result}")


def is_open(char: str) -> bool:
    open_chars = set(['(', '[', '{', '<'])
    if char in open_chars:
        return True
    else:
        return False


def is_matching_braces(open: str, close:str) -> bool:
    if open == '(' and close == ')':
        return True
    elif open == '[' and close == ']':
        return True
    elif open == '{' and close == '}':
        return True
    elif open == '<' and close == '>':
        return True
    else:
        return False


def get_matching_brace(open: str) -> str:
    if open == '(':
        return ')'
    elif open == '{':
        return '}'
    elif open == '[':
        return ']'
    else:
        return '>'


if __name__ == "__main__":
    part1()
    part2()