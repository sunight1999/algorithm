N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    start = 0
    end = N - 1
    find = False
    while start <= end:
        mid = int((start + end) / 2)
        if nums[mid] == target:
            print(1)
            find = True
            break
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    if find is False:
        print(0)
