import sys
import heapq
input = sys.stdin.readline

N = int(input())
decks = []
for _ in range(N):
    heapq.heappush(decks, int(input()))

count = 0
while len(decks) > 1:
    min1 = heapq.heappop(decks)
    min2 = heapq.heappop(decks)

    sum = min1 + min2
    count += sum
    heapq.heappush(decks, sum)

print(count)