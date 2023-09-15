import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * n

for i in range(n):
    nums[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(n):
    su = nums[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)