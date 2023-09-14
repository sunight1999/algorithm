import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
k -= 1

def swap(i, j):
    global nums
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def quick(start, end):
    global k
    global nums

    pivot = (start + end) // 2
    swap(start, pivot)
    pivotv = nums[start]
    l = start + 1
    r = end

    if l == end:
        if nums[start] > nums[end]:
            swap(start, end)
        return

    while l <= r:
        while nums[l] < pivotv and l < n - 1:
            l += 1
        while nums[r] > pivotv and r > 0:
            r -= 1

        if l <= r:
            swap(l, r)
            l += 1
            r -= 1
            
    nums[start] = nums[r]
    nums[r] = pivotv
    pivot = r

    if pivot == k:
        return
    elif pivot > k:
        quick(start, pivot - 1)
    else:
        quick(pivot + 1, end)

quick(0, len(nums) - 1)

print(nums[k])