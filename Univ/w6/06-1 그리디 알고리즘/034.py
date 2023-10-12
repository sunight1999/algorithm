from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
positives = PriorityQueue()
negatives = PriorityQueue()
zeros = 0
ones = 0

for _ in range(N):
    n = int(input())
    if n > 1:
        positives.put(-n)
    elif n < 0:
        negatives.put(n)
    elif n == 0:
        zeros += 1
    else:
        ones += 1

sum = 0

while positives.qsize() > 1:
    sum += -positives.get() * -positives.get()

if positives.qsize() > 0:
    sum += -positives.get()

while negatives.qsize() > 1:
    sum += negatives.get() * negatives.get()

if negatives.qsize():
    if zeros == 0:
        sum += negatives.get()

sum += ones
print(sum)