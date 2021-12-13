from collections import defaultdict

from util.fileutil import read_file_to_string_list


class Node:
    def __init__(self, name: str, big: bool):
        self.name = name
        self.big = big
        self.neighbors = set()

    def __str__(self):
        return f"{self.name} - {self.neighbors}"

    def add_neighbor(self, neighbor: str):
        self.neighbors.add(neighbor)


def find_all_paths(graph: {}, source: str, dest: str, visited: {}, route: [], routes: []):
    visited[source] = True
    route.append(source)

    if source == dest:
        routes.append(route.copy())
    else:
        for i in graph[source].neighbors:
            if visited[i] is False or graph[i].big:
                find_all_paths(graph, i, dest, visited, route, routes)

    route.pop()
    visited[source] = False


def find_all_paths2(graph: {}, source: str, dest: str, visited: {}, route: [], routes: [], two_steps: str):
    visited[source] += 1
    route.append(source)

    if source == dest:
        routes.append(route.copy())
    else:
        for i in graph[source].neighbors:
            if visited[i] == 0 or (i == two_steps and visited[i] == 1) or graph[i].big:
                find_all_paths2(graph, i, dest, visited, route, routes, two_steps)

    route.pop()
    visited[source] -= 1


def part1() -> None:
    vals = read_file_to_string_list("data.txt")
    graph = {}
    for row in vals:
        first, second = row.split('-', 1)
        # print(f"{first} and then {second}")
        if first not in graph:
            node = Node(first, first.isupper())
            node.neighbors.add(second)
            graph[first] = node
        else:
            graph[first].neighbors.add(second)

        if second not in graph:
            node = Node(second, second.isupper())
            node.neighbors.add(first)
            graph[second] = node
        else:
            graph[second].neighbors.add(first)

    routes = []
    visited = defaultdict(bool)
    route = []
    find_all_paths(graph, 'start', 'end', visited, route, routes)
    for path in routes:
        print(",".join(path))

    print(f"Number of paths is {len(routes)}")


def part2() -> None:
    vals = read_file_to_string_list("data.txt")
    graph = {}
    for row in vals:
        first, second = row.split('-', 1)
        # print(f"{first} and then {second}")
        if first not in graph:
            node = Node(first, first.isupper())
            node.neighbors.add(second)
            graph[first] = node
        else:
            graph[first].neighbors.add(second)

        if second not in graph:
            node = Node(second, second.isupper())
            node.neighbors.add(first)
            graph[second] = node
        else:
            graph[second].neighbors.add(first)

    routes = []
    visited = defaultdict(int)
    route = []
    for lower in graph:
        if lower != 'start' and lower != 'end' and lower.islower():
            find_all_paths2(graph, 'start', 'end', visited, route, routes, lower)
    final_routes = set()
    for path in routes:
        final_routes.add(",".join(path))

    print(f"Number of paths is {len(final_routes)}")


if __name__ == "__main__":
    part1()
    part2()
