

A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            sum = 500*i +100*j + k*50
            if sum == X:
                count += 1
            

print(count)

