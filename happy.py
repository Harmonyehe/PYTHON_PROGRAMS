def sum_of_dig(s):
    sum=0   
    while s>0:
        d=s%10
        sum=sum+(d*d)
        s=s//10
    return sum

def happy(num):
    while num>9:
        num=sum_of_dig(num)
        print(num,end=' ')
        if num==1:
            return True
    return False


a=int(input("Enter Value:"))
if happy(a):
    print("\nIs a happy num")
else:
    print("\nIs not a happy num")