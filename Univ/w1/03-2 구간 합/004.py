import sys
input = sys.stdin.readline

size, queryCount = map(int, input().split())
table = [[0 for j in range(size + 1)] for i in range(size + 1)]
sumTable = [[0 for j in range(size + 1)] for i in range(size + 1)]

for i in range(1, size + 1):
    row = list(map(int, input().split()))
    for j in range(1, size + 1):
        table[i][j] = row[j - 1]

for i in range(1, size + 1):
    for j in range(1, size + 1):
        sumTable[i][j] = sumTable[i][j - 1] + sumTable[i - 1][j] - sumTable[i - 1][j - 1] + table[i][j]

for i in range(queryCount):
    sum = 0
    x1, y1, x2, y2 = map(int, input().split())
    print(sumTable[x2][y2] - sumTable[x1 - 1][y2] - sumTable[x2][y1 - 1] + sumTable[x1 - 1][y1 - 1])