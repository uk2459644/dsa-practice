import math 

for i in range(int(input())):
    N,M=[int(z) for z in input().strip().split()]
    A = [int(z) for z in input()]
    summer = sum(A)
    if summer==0:
        print(N*M)
    else:
        tot_sum = summer*M
        if tot_sum%2==1:
            print(0)
        else:
            if M%2 == 1:
                counter = 0
                temp_sum =0
                for i in range(N):
                    temp_sum+=A[i]
                    if temp_sum == summer/2:
                        counter+=1 
                print(counter)
            else:
                arr1 = A+A
                counter=0
                temp_sum=0
                for i in range(2*N):
                    temp_sum+=arr1[i]
                    if temp_sum == summer:
                        counter+=1 
                print(counter)