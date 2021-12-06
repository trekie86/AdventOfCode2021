from util.fileutil import read_file_to_string_list
from collections import Counter
import numpy as np


def part1() -> None:
    lanternfish_evolution2("data.txt", 80)


def part2() -> None:
    lanternfish_evolution2("data.txt", 256)


def lanternfish_evolution2(input_file, days):
    """
    I feel there is likely some way to make this a little cleaner in terms of orgnanization it works quite well.
    """
    vals = read_file_to_string_list(input_file)
    fish_counter = Counter([int(i) for i in vals[0].split(',')])
    fish = dict(fish_counter)
    for day in range(1, days + 1):
        if day % 10 == 0:
            print(f"Currently evolving on day {day}")
        new_fish = dict()
        new_fish[8] = fish.get(0, 0)
        new_fish[7] = fish.get(8, 0)
        new_fish[6] = fish.get(7, 0) + fish.get(0, 0)
        new_fish[5] = fish.get(6, 0)
        new_fish[4] = fish.get(5, 0)
        new_fish[3] = fish.get(4, 0)
        new_fish[2] = fish.get(3, 0)
        new_fish[1] = fish.get(2, 0)
        new_fish[0] = fish.get(1, 0)

        fish = new_fish

    print(f"After day {days} there are {sum(fish.values())}")


def lanternfish_evolution1(input_file, days):
    """
    My first attempt and although it would work, it's way too expensive computationally and memory wise.
    """
    vals = read_file_to_string_list(input_file)
    fish = np.array([int(i) for i in vals[0].split(',')])
    for day in range(1, days + 1):
        if day % 10 == 0:
            print(f"Currently evolving on day {day}")
        new_fish = np.array([8] * np.count_nonzero(fish == 0))
        fish = fish - 1
        fish = np.where(fish == -1, 6, fish)
        fish = np.append(fish, new_fish)

    print(f"After day {days} there are {len(fish)}")


if __name__ == "__main__":
    part1()
    part2()
