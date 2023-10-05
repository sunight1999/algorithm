N, M = map(int, input().split())
minutes = list(map(int, input().split()))
start = 0
end = 0

for i in minutes:
    if start < i:
        start = i
    end += i

while start <= end:
    mid = int((start + end) / 2)
    count = 0
    sum = 0
    for min in minutes:
        if sum + min > mid:
            count += 1
            sum = 0
        sum += min
    
    if sum != 0:
        count += 1

    if count > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)