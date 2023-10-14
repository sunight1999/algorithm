from queue import PriorityQueue
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
s = int(input())
g = []

for i in range(V + 1):
    g.append([])

for _ in range(E):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

included = [False for _ in range(V + 1)]
distance = [float('INF') for _ in range(V + 1)]
distance[s] = 0
previous = [-1 for _ in range(V + 1)]
previous[s] = 0

openedHeap = PriorityQueue()
for w, wt in g[s]:
    openedHeap.put((wt, s, w))

cur = s
while openedHeap.qsize() > 0:
    m = -1

    min_target = openedHeap.get()
    m = min_target[2]

    included[cur] = True

    for w, wt in g[m]:
        if not included[w] and distance[cur] + wt < distance[w]:
            distance[w] = distance[cur] + wt
            previous[w] = cur

        openedHeap.put((wt, cur, w))
    cur = m


for i in range(1, V + 1):
    if distance[i] == float('INF'):
        print('INF')
    else:
        print(distance[i])