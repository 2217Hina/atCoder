# TLE

count = 0
N = int(input())
ints = list(map(int,input().split()))
odd = False

while True:
    for i in range(N):
        if ints[i] % 2 == 0:
            ints[i] = ints[i]/2
        else:
            odd = True
            break
    if odd == False:
        count += 1
    else:
        print(count)

