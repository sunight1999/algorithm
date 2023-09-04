from collections import deque

count, window = map(int, input().split())
nums = list(map(int, input().split()))
myDeque = deque()

for i in range(count):
    while myDeque and myDeque[-1][1] > nums[i]:
        myDeque.pop()

    myDeque.append((i, nums[i]))

    if myDeque[0][0] <= i - window:
        myDeque.popleft()
    
    print(myDeque[0][1], end=' ')