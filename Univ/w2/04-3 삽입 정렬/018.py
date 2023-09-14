n = int(input())
nums = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if nums[j] < nums[j - 1]:
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp
        else:
            break

time = 0
sum = 0
for i in range(n):
    time = time + nums[i]
    sum = sum + time

print(sum)