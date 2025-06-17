def miss_num(num):
    n=len(num)
    exp_sum=(n*(n+1))//2
    real_sum=0
    for i in num:
        real_sum+=i
    return exp_sum-real_sum

inp=input("enter :")
num=list(map(int,inp.strip().split()))
print("Missing num is : ",miss_num(num))