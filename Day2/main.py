from util.fileutil import read_file_to_string_list

def part1() -> None:
    vals: list[str] = read_file_to_string_list("part1data.txt")
    depth: int = 0
    position: int = 0

    val: str
    for val in vals:
        operator: str = val.split()[0]
        amount: int = int(val.split()[1])

        if operator == 'forward':
            position += amount
        elif operator == 'down':
            depth += amount
        elif operator == 'up':
            depth -= amount

    print(f"Final depth is {depth}, final position is {position}. Product is {depth * position}")



def part2() -> None:
    vals: list[str] = read_file_to_string_list("part1data.txt")
    depth: int = 0
    position: int = 0
    aim: int = 0

    val: str
    for val in vals:
        operator: str = val.split()[0]
        amount: int = int(val.split()[1])

        if operator == 'forward':
            position += amount
            depth += aim * amount
        elif operator == 'down':
            aim += amount
        elif operator == 'up':
            aim -= amount

    print(f"Final depth is {depth}, final position is {position}. Product is {depth * position}")


if __name__ == '__main__':
    part1()
    part2()