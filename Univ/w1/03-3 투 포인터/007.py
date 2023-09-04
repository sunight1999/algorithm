num = int(input())
M = int(input())
ingredients = list(map(int, input().split()))
ingredients.sort()

start = 0
end = num - 1
sum = count = 0

while start < end:
    sum = ingredients[start] + ingredients[end]

    if sum > M:
        end -= 1
    elif sum == M:
        count += 1
        start += 1
        end -= 1
    else:
        start += 1

print(count)