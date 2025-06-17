a=list(map(int,input("ENetr :").split()))
print(a)
sums=0
for i in a:
    sums+=i
print(sums)
maxi=a[0]

for i in a:
    if i>maxi:
        maxi=i
    
print(maxi)

