def sum_of(s):
    sum=0
    while s>0:
        num=s%10
        sum+=num
        s=s//10
    return sum


inp=int(input("Enter :"))
print("Sum of Digits of num is :",sum_of(inp))
