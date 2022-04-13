

from __future__ import annotations

Path = list[tuple[int, int]]

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
]

delta = ([-1, 0], [0, -1], [1, 0], [0, 1])  


class Node:
    

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        goal_x: int,
        goal_y: int,
        g_cost: float,
        parent: Node | None,
    ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_y, pos_x)
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.g_cost = g_cost
        self.parent = parent
        self.f_cost = self.calculate_heuristic()

    def calculate_heuristic(self) -> float:
        
        dy = abs(self.pos_x - self.goal_x)
        dx = abs(self.pos_y - self.goal_y)
        return dx + dy

    def __lt__(self, other) -> bool:
        return self.f_cost < other.f_cost


class GreedyBestFirst:
    

    def __init__(self, start: tuple[int, int], goal: tuple[int, int]):
        self.start = Node(start[1], start[0], goal[1], goal[0], 0, None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], 99999, None)

        self.open_nodes = [self.start]
        self.closed_nodes: list[Node] = []

        self.reached = False

    def search(self) -> Path | None:
        
        while self.open_nodes:
            
            self.open_nodes.sort()
            current_node = self.open_nodes.pop(0)

            if current_node.pos == self.target.pos:
                self.reached = True
                return self.retrace_path(current_node)

            self.closed_nodes.append(current_node)
            successors = self.get_successors(current_node)

            for child_node in successors:
                if child_node in self.closed_nodes:
                    continue

                if child_node not in self.open_nodes:
                    self.open_nodes.append(child_node)
                else:
                    
                    better_node = self.open_nodes.pop(self.open_nodes.index(child_node))

                    if child_node.g_cost < better_node.g_cost:
                        self.open_nodes.append(child_node)
                    else:
                        self.open_nodes.append(better_node)

        if not self.reached:
            return [self.start.pos]
        return None

    def get_successors(self, parent: Node) -> list[Node]:
        
        successors = []
        for action in delta:
            pos_x = parent.pos_x + action[1]
            pos_y = parent.pos_y + action[0]

            if not (0 <= pos_x <= len(grid[0]) - 1 and 0 <= pos_y <= len(grid) - 1):
                continue

            if grid[pos_y][pos_x] != 0:
                continue

            successors.append(
                Node(
                    pos_x,
                    pos_y,
                    self.target.pos_y,
                    self.target.pos_x,
                    parent.g_cost + 1,
                    parent,
                )
            )
        return successors

    def retrace_path(self, node: Node | None) -> Path:
        
        current_node = node
        path = []
        while current_node is not None:
            path.append((current_node.pos_y, current_node.pos_x))
            current_node = current_node.parent
        path.reverse()
        return path


if __name__ == "__main__":
    init = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    for elem in grid:
        print(elem)

    print("------")

    greedy_bf = GreedyBestFirst(init, goal)
    path = greedy_bf.search()
    if path:
        for pos_x, pos_y in path:
            grid[pos_x][pos_y] = 2

        for elem in grid:
            print(elem)
