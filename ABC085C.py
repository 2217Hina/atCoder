def flag(N,Y):
    for i in range(N+1):
        A = 10000*i

        for j in range(N-i+1):
            B = 5000*j
            k = N-i-j
            C = 1000*k

            if Y == A + B + C:
                print(i,j,k)
                return;
    print(-1,-1,-1)  

N, Y = map(int, input().split())

flag(N,Y)


            



            

# import sys

# N, Y = map(int, input().split())

# for i in range(N+1):
#     A = 10000*i

#     for j in range(N-i+1):
#         B = 5000*j
#         k = N-i-j
#         C = 1000*k

#         if Y == A + B + C:
#             print(i,j,k)
#             sys.exit()


# print(-1,-1,-1)

            

