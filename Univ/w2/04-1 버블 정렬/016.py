import sys
input = sys.stdin.readline

num = int(input())
nums = []

for i in range(num):
    nums.append((int(input()), i))

sorted = sorted(nums)

max = 0
for i in range(num):
    diff = sorted[i][1] - i
    if diff > max:
        max = diff

print(max + 1)