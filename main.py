import graph


def main():
    g = graph.Graph()
    g.add_edge((0, 1))
    g.add_edge((0, 5))
    g.add_edge((1, 2))
    g.add_edge((3, 1))
    g.add_edge((3, 2))
    g.add_edge((4, 3))
    g.add_edge((4, 6))
    g.add_edge((1, 4))
    g.add_edge((2, 5))
    print(g.graf)
    g.dfs(1)
    print(g.list_of_visited)
    g.bfs(1)
    print(g.list_of_visitedq)

if __name__ == "__main__":
    main()