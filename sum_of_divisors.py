def sum_div(s):
    sums=0
    for i in range(1,s+1):
        if s%i==0:
            print(i,end=' ')
            sums+=i
            
    return sums

a=int(input("Enter num: "))
print("Ans :",sum_div(a))