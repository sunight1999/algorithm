N = int(input())
start = end = 1
sum = 0
count = 1

while start < N:
    if (sum >= N):
        if (sum == N):
            count += 1
        sum -= start
        start += 1

        continue

    sum += end
    end += 1

print(count)