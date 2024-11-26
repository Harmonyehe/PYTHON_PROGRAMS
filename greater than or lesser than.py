lst=[]
n=int(input("Enter: "))
for i in range(0,n):
    ele=int(input("Enter value"))
    lst.append(ele)

print("list is:",lst)

for i in lst:
    if i>5:
        print("value greater than 5")
    else:
        print("value less than 5")

"""sums=0
for i in lst:
    sums+=i

print("sum of list:",sums)"""


