from queue import PriorityQueue
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
s = int(input())
g = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

visited = [False for _ in range(V + 1)]
distance = [float('INF') for _ in range(V + 1)]
distance[s] = 0

openedHeap = PriorityQueue()
openedHeap.put((0, s))

while openedHeap.qsize() > 0:
    cur = openedHeap.get()
    cur_v = cur[1]

    if visited[cur_v]:
        continue

    visited[cur_v] = True

    for v, w in g[cur_v]:
        if distance[cur_v] + w < distance[v]:
            distance[v] = distance[cur_v] + w
            openedHeap.put((distance[v], v))


for i in range(1, V + 1):
    if distance[i] == float('INF'):
        print('INF')
    else:
        print(distance[i])