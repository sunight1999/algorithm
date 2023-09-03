num = int(input())
scores = input().split()
max = 0
sum = 0

for score in scores:
    val = int(score)
    if (val > max):
        max = val
    sum += val

print(sum / (num * max) * 100)