import sys
import math
input = sys.stdin.readline

n = int(input())
counts = [0] * 10001

for _ in range(n):
    v = int(input())
    counts[v] += 1

for i in range(10001):
    for j in range(counts[i]):
        print(i)