import sys
import math
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sorted = [0] * n
bubble = 0

def swap(i, j):
    global nums
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def merge(start, end):
    global sorted
    global nums
    global bubble

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
                bubble += pivot - idx1
            else:
                key = nums[idx1]
                idx1 += 1

        sorted[i] = key

    for i in range(start, end + 1):
        nums[i] = sorted[i]

merge(0, n - 1)

print(bubble)