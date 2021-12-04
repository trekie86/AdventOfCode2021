from itertools import groupby


def split_lists_by_whitespace(in_list: []) -> list[[]]:
    """
    Takes a given list and splits it by a whitespace and returns a list of lists.
    @param in_list: The list to split.
    @return: The list of lists that were separated by whitespace.
    """
    return [list(sub) for ele, sub in groupby(in_list, key=bool) if ele]