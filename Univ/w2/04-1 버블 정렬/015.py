num = int(input())
nums = [0] * num

for i in range(num):
    nums[i] = int(input())

for i in range(num - 1):
    for j in range(1, num - i):
        if nums[j - 1] > nums[j]:
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp

for i in range(num):
    print(nums[i])