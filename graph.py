import que
import stack

s = stack.Stack()
q = que.Queue()


class Graph(object):

    def __init__(self):
        self.graf = {}
        self.list_of_visited = []
        self.list_of_visitedq = []

    def add_node(self, node):
        if node not in self.graf:
            self.graf[node] = []

    def add_edge(self, edge):
        node1, node2 = edge
        self.add_node(node1)
        self.add_node(node2)
        if node2 not in self.graf[node1]:
            self.graf[node1].append(node2)

    def dfs(self, node):
        if not (self.list_of_visited):
            s.push(node)
        if node not in self.list_of_visited:
            self.list_of_visited.append(node)
        if self.graf[node] and not (all(el in self.list_of_visited for el in self.graf[node])):
            for element in self.graf[node]:
                if element not in self.list_of_visited:
                    s.push(node)
                    self.dfs(element)
        else:
            s.pop()
            if s.empty():
                print('DFS')
                return
            self.dfs(s.top())

    def bfs(self, node):
        self.list_of_visitedq.append(node)
        if self.graf[node] and not (all(el in self.list_of_visitedq for el in self.graf[node])):
            for element in self.graf[node]:
                if element not in self.list_of_visitedq:
                    q.push(element)
            visited = q.pop()

            self.bfs(visited)
        else:
            if q.empty():
                print('BFS')
                return
            self.bfs(q.pop())
