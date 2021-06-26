graph = {}
computer = int(input())
edge = int(input())

for i in range(edge):
    edge_number = input().split(' ')
    c1, c2 = map(int, edge_number)
    
    if c1 not in graph:
        graph[c1] = [c2]
    elif c2 not in graph[c1]:
        graph[c1].append(c2)

    if c2 not in graph:
        graph[c2] = [c1]
    elif c1 not in graph[c2]:
        graph[c2].append(c1)


def BFS(graph):
    visited = []
    queue = [1]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort()
                queue += tmp
    return len(visited)
  
print(BFS(graph)-1)