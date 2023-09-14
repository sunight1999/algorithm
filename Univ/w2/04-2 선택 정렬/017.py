nums = list(input())
n = len(nums)

for i in range(n):
    max = i
    for j in range(i + 1, n):
        if nums[max] < nums[j]:
            max = j
    
    temp = nums[i]
    nums[i] = nums[max]
    nums[max] = temp

for i in range(n):
    print(nums[i], end="")