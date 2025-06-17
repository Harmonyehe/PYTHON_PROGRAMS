def miss_num(s):
    n=len(s)
    exp_sum=n*(n+1)//2
    real_sum=0
    for i in s:
        real_sum+=i

    return exp_sum-real_sum

s=list(map(int,input("Enter the numbers with space: ").strip().split()))
print("Missing number is : ",miss_num(s))