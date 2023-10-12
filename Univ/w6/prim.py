import heapq

def search_connected_nodes(i):
    visited[i] = True
    for node in g[i]:
        if node[1] != i:
            n = (node[0], node[1], i)
            heapq.heappush(opened, n)

N = 7
g = [[] for _ in range(N)]
g[0] = [(9, 1), (10, 2)]
g[1] = [(9, 0), (10, 3), (5, 4), (3, 6)]
g[2] = [(10, 0), (9, 3), (7, 4), (2, 5)]
g[3] = [(10, 1), (9, 2), (4, 5), (8, 6)]
g[4] = [(5, 1), (7, 2), (1, 6)]
g[5] = [(2, 2), (4, 3), (6, 6)]
g[6] = [(3, 1), (8, 3), (1, 4), (6, 5)]

result = [[] for _ in range(N)]
visited = [False] * N
opened = []

search_connected_nodes(0)

while len(opened) > 0:
    target = heapq.heappop(opened)

    if visited[target[1]] == True:
        continue

    result[target[2]].append((target[0], target[1]))
    result[target[1]].append((target[0], target[2]))
    search_connected_nodes(target[1])

print(result)