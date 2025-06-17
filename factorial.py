def fact(s):
    temp=1
    if(s==0):
        return 1
    else:
        for i in(1,s+1):
            temp*=i

            
        return temp

inp=int(input("Enter num :"))
print("The ans is :",fact(inp))

