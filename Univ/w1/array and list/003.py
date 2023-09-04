import sys
input = sys.stdin.readline

numCount, queryCount = map(int, input().split())
nums = list(map(int, input().split()))

sectionSumArr = [nums[0]]
for i in range(1, numCount):
    sectionSumArr.append(sectionSumArr[i - 1] + nums[i])

for i in range(0, queryCount):
    begin, end = map((lambda x: int(x) - 1), input().split())
    print(sectionSumArr[end] - (0 if begin == 0 else sectionSumArr[begin - 1]))