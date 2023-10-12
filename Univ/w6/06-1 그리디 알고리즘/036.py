from queue import PriorityQueue
import sys
input = sys.stdin.readline

answer = 0
A = list(map(str, input().split("-")))

def sum(str):
    sum = 0
    temp = str.split("+")
    for snum in temp:
        sum += int(snum)

    return sum

for i in range(len(A)):
    temp = sum(A[i])
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)