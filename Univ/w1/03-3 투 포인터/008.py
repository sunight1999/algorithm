import sys
input = sys.stdin.readline

total = int(input())
nums = list(map(int, input().split()))
nums.sort()

count = 0
for i in range(total):
    start = 0
    end = total - 1
    while start < end:
        sum = nums[start] + nums[end]
        target = nums[i]

        if sum > target:
            end -= 1
        elif sum == target:
            if start == i or end == i:
                if start == i:
                    start += 1
                else:
                    end -= 1
                continue
            
            count += 1
            break
        else:
            start += 1

print(count)