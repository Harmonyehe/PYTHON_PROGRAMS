def rev_fun(s):
    temp=0
    while s>0:
        num=s%10
        temp=temp*10+num
        s=s//10
    return temp


a=int(input("ENter the number :"))
print("Reverse of the number is :",rev_fun(a))