import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = [0] * n
sorted = [0] * n
for i in range(n):
    nums[i] = int(input())

def swap(i, j):
    global nums
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def merge(start, end):
    global sorted
    global nums

    if end - start <= 0:
        return

    pivot = math.ceil((start + end) / 2)

    merge(start, pivot - 1)
    merge(pivot, end)

    idx1 = start
    idx2 = pivot
    for i in range(start, end + 1):
        if idx1 >= pivot:
            key = nums[idx2]
            idx2 += 1
        elif idx2 > end:
            key = nums[idx1]
            idx1 += 1
        else:
            if nums[idx1] > nums[idx2]:
                key = nums[idx2]
                idx2 += 1
            else:
                key = nums[idx1]
                idx1 += 1

        sorted[i] = key

    for i in range(start, end + 1):
        nums[i] = sorted[i]

merge(0, n - 1)

for i in range(n):
    print(str(nums[i]) + '\n')