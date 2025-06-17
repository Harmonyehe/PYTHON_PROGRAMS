def armstrong(s):
    str_num=str(s)
    pow=len(str_num)
    arm=0

    for i in str_num:
        arm+=int(i)**pow

    return arm

a=int(input("Enter number: "))
if armstrong(a)==a:
    print("YES")

else:
    print("NO")