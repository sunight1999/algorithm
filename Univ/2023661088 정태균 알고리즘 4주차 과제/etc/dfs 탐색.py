adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
n = len(adj_list)
visited = [False for _ in range(n + 1)]

def dfs(v):
    visited[v] = True
    print(v, ' ', end='')
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)

print('DFS 방문 순서')
for i in range(n):
    if not visited[i]:
        dfs(i)