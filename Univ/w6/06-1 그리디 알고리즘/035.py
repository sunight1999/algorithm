from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())

discussions = PriorityQueue()
for _ in range(N):
    begin, end = map(int, input().split())
    discussions.put((end, begin))

count = 0
end = 0
while discussions.qsize() > 0:
    d = discussions.get()
    if d[1] >= end:
        count += 1
        end = d[0]

print(count)