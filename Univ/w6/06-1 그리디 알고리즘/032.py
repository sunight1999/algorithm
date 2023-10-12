import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0
current = K
for i in range(N - 1, -1, -1):
    count += current // coins[i]
    current = current % coins[i]

    if current == 0:
        break

print(count)