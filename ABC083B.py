N,A,B = map(int,input().split())
XYZ = []


for i in range(N+1):
    array = list(map(int,str(i)))
    if A <= sum(array) and sum(array) <= B:
        XYZ.append(i)

answer = sum(XYZ)    
 
print(answer)




