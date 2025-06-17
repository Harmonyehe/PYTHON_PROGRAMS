def pali(s):
    original=s
    temp=0
    while s>0:
        num=s%10
        temp=temp*10+num
        s=s//10
    if temp==original:
        print("It is a palindrome")
    else:
        print("Not a palindrome")    


inp=int(input("Enter num :"))
pali(inp)