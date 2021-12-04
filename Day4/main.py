from util.fileutil import read_file_to_string_list
from util.list_util import split_lists_by_whitespace


class Entry:
    def __init__(self, value: int):
        self.value: int = int(value)
        self.marked: bool = False

    def __str__(self):
        return f"val: {self.value}, marked: {self.marked}"


class PlayBoard:
    def __init__(self, grid):
        self.board: Entry[[]] = []
        for row in grid:
            self.board.append([Entry(x) for x in row.split()])
        self.done = False
        self.row_count = len(grid)
        self.col_count = len(grid[0].split())
        self.rows_marked = [0] * self.row_count
        self.cols_marked = [0] * self.col_count

    def __str__(self):
        res = ""
        for r in self.board:
            for c in r:
                res += str(c) + " "
            res += "\n"
        return res

    def print(self):
        for r in self.board:
            for c in r:
                print(str(c.value), end=" ")
            print()

    def sumAllUnmarked(self) -> int:
        total = 0
        for r in self.board:
            for c in r:
                if not c.marked:
                    total += c.value
        return total

    def markValue(self, play_val):
        for r_idx, r in enumerate(self.board):
            for c_idx, c in enumerate(r):
                if c.value == play_val:
                    c.marked = True
                    self.rows_marked[r_idx] += 1
                    self.cols_marked[c_idx] += 1
                    # Short circuit and return
                    return

    def hasWinner(self) -> bool:
        for r in self.rows_marked:
            if r == self.col_count:
                return True
        for c in self.cols_marked:
            if c == self.row_count:
                return True
        return False


def part1() -> None:
    vals = read_file_to_string_list("data.txt")
    play_vals = [int(x) for x in vals[0].split(',')]
    raw_boards = split_lists_by_whitespace(vals[2:])
    boards = [PlayBoard(grid) for grid in raw_boards]

    game_over = False
    for play_idx, play in enumerate(play_vals):
        if game_over:
            return
        for board in boards:
            board.markValue(play)
            # No point in checking winners if we haven't had at least 5 plays
            if play_idx >= 4:
                if board.hasWinner():
                    unmarked_sum = board.sumAllUnmarked()
                    winning = play * unmarked_sum
                    print(f"Unmakred sum: {unmarked_sum}, and last play {play}")
                    print(f"The winning value is {winning}")
                    game_over = True
                    break


def part2() -> None:
    vals = read_file_to_string_list("data.txt")
    play_vals = [int(x) for x in vals[0].split(',')]
    raw_boards = split_lists_by_whitespace(vals[2:])
    boards = [PlayBoard(grid) for grid in raw_boards]

    winners = []
    for play_idx, play in enumerate(play_vals):
        for board in boards:
            if not board.done:
                board.markValue(play)
                # No point in checking winners if we haven't had at least 5 plays
                if play_idx >= 4:
                    if board.hasWinner():
                        unmarked_sum = board.sumAllUnmarked()
                        winning = play * unmarked_sum
                        winners.append(
                            f"Unmakred sum: {unmarked_sum}, and last play {play}\nThe winning value is {winning}")
                        # Mark the board as done so we don't continue playing on the board
                        board.done = True
    print(winners[-1])


if __name__ == "__main__":
    print("Part 1\n")
    part1()
    print("\nPart 2\n")
    part2()