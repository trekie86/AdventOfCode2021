import sys

from util.fileutil import read_line_single_line_to_ints


def part1() -> None:
    vals = read_line_single_line_to_ints("data.txt")
    vals.sort()

    # Get the value right in the middle of the sorted array
    x = vals[len(vals) // 2]

    sums = 0

    # Calculate the minimized sums
    for i in range(len(vals)):
        sums += abs(vals[i] - x)

    # Return the required sums
    print(f"Optimal location is {x} with summed difference of {sums}")


def part2() -> None:
    vals = read_line_single_line_to_ints("data.txt")
    vals.sort()

    # Start with a max value to compare against
    min_fuel = sys.maxsize
    # Start at the median and work up until the fuel cost hits the minima
    x = vals[len(vals) // 2]
    dp_sums = {}

    for x in range(x, len(vals)):
        sums = 0
        # Calculate the minimized sums
        for i in range(len(vals)):
            sums += dynamic_sum(dp_sums, abs(vals[i] - x))
        if sums > min_fuel:
            break
        else:
            min_fuel = sums

    # Return the required sums
    print(f"Optimal location is {x-1} with summed difference of {min_fuel}")


def dynamic_sum(dp_sums: {}, val: int) -> int:
    if val in dp_sums:
        return dp_sums[val]
    else:
        rolling_sum = 0
        for i in range(val, 0, -1):
            rolling_sum += i
        dp_sums[val] = rolling_sum
        return rolling_sum


if __name__ == "__main__":
    part1()
    part2()
