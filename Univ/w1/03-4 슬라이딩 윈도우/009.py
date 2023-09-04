a = c = g = t = 0
def countDna(char, add = True):
    global a, c, g, t
    val = 1 if add == True else -1

    if char == 'A':
        a += val
    elif char == 'C':
        c += val
    elif char == 'G':
        g += val
    elif char == 'T':
        t += val

dnaLen, winLen = map(int, input().split())
dna = input()
A, C, G, T = map(int, input().split())

count = 0

for i in range(0, winLen):
    countDna(dna[i])

for i in range(0, dnaLen - winLen + 1):
    if a >= A and c >= C and g >= G and t >= T:
        count += 1
    
    if i + winLen >= dnaLen:
        break

    countDna(dna[i], False) 
    countDna(dna[i + winLen])

print(count)
