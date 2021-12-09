from collections import deque
import numpy
from util.fileutil import read_file_to_string_list


def part1() -> None:
    vals = read_file_to_string_list("data.txt")
    grid = []
    for row in vals:
        grid.append([int(i) for i in row])
    mins = []
    max_y = len(grid)-1
    max_x = len(grid[0])-1
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            current_val = grid[y][x]
            if y == 0:
                if x == 0:
                    if current_val < grid[y+1][x] and current_val < grid[y][x+1]:
                        mins.append(current_val)
                elif x < max_x:
                    if current_val < grid[y+1][x] and current_val < grid[y][x+1] and current_val < grid[y][x-1]:
                        mins.append(current_val)
                else:
                    if current_val < grid[y+1][x] and current_val < grid[y][x-1]:
                        mins.append(current_val)
            elif y < max_y:
                if x == 0:
                    if current_val < grid[y-1][x] and current_val < grid[y+1][x] and current_val < grid[y][x+1]:
                        mins.append(current_val)
                elif x < max_x:
                    if current_val < grid[y+1][x] and current_val < grid[y-1][x] and current_val < grid[y][x-1] and current_val < grid[y][x+1]:
                        mins.append(current_val)
                else:
                    if current_val < grid[y+1][x] and current_val < grid[y-1][x] and current_val < grid[y][x-1]:
                        mins.append(current_val)
            else:
                if x == 0:
                    if current_val < grid[y-1][x] and current_val < grid[y][x+1]:
                        mins.append(current_val)
                elif x < max_x:
                    if current_val < grid[y - 1][x] and current_val < grid[y][x - 1] and current_val < grid[y][x + 1]:
                        mins.append(current_val)
                else:
                    if current_val < grid[y - 1][x] and current_val < grid[y][x - 1]:
                        mins.append(current_val)
    print(f"Found {len(mins)} low points")
    print(f"Sum of minimum values 1+ height is {sum(mins) + len(mins)}")


def part2() -> None:
    vals = read_file_to_string_list("data.txt")
    grid = []
    for row in vals:
        grid.append([int(i) for i in row])
    mins = []
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            current_val = grid[y][x]
            if y == 0:
                if x == 0:
                    if current_val < grid[y + 1][x] and current_val < grid[y][x + 1]:
                        mins.append((y,x))
                elif x < max_x:
                    if current_val < grid[y + 1][x] and current_val < grid[y][x + 1] and current_val < grid[y][x - 1]:
                        mins.append((y,x))
                else:
                    if current_val < grid[y + 1][x] and current_val < grid[y][x - 1]:
                        mins.append((y,x))
            elif y < max_y:
                if x == 0:
                    if current_val < grid[y - 1][x] and current_val < grid[y + 1][x] and current_val < grid[y][x + 1]:
                        mins.append((y,x))
                elif x < max_x:
                    if current_val < grid[y + 1][x] and current_val < grid[y - 1][x] and current_val < grid[y][
                        x - 1] and current_val < grid[y][x + 1]:
                        mins.append((y,x))
                else:
                    if current_val < grid[y + 1][x] and current_val < grid[y - 1][x] and current_val < grid[y][x - 1]:
                        mins.append((y,x))
            else:
                if x == 0:
                    if current_val < grid[y - 1][x] and current_val < grid[y][x + 1]:
                        mins.append((y,x))
                elif x < max_x:
                    if current_val < grid[y - 1][x] and current_val < grid[y][x - 1] and current_val < grid[y][x + 1]:
                        mins.append((y,x))
                else:
                    if current_val < grid[y - 1][x] and current_val < grid[y][x - 1]:
                        mins.append((y,x))

    print(f"Found {len(mins)} low points, calculating basins")
    basins = []
    for star_y, start_x in mins:
        basin = set()
        traversal_q = deque()
        traversal_q.append((star_y, start_x))
        while traversal_q:
            current_y, current_x = traversal_q.pop()
            if (current_y, current_x) not in basin:
                basin.add((current_y, current_x))
                current_val = grid[current_y][current_x]
                if 0 < current_y:
                    if current_val < grid[current_y - 1][current_x] != 9:
                        traversal_q.append((current_y - 1, current_x))
                if current_y < max_y:
                    if current_val < grid[current_y + 1][current_x] != 9:
                        traversal_q.append((current_y + 1, current_x))
                if current_x < max_x:
                    if current_val < grid[current_y][current_x + 1] != 9:
                        traversal_q.append((current_y, current_x + 1))
                if 0 < current_x:
                    if current_val < grid[current_y][current_x - 1] != 9:
                        traversal_q.append((current_y, current_x - 1))
        basins.append(basin)
    basin_sizes = [len(basin) for basin in basins]
    basin_sizes.sort(reverse=True)
    prod = numpy.prod(basin_sizes[:3])
    print(f"Product of biggest basins is {prod}")






if __name__ == "__main__":
    part1()
    part2()