l=[]
inp=int(input("enter:"))
for i in range(0,inp):
        ele=int(input("enter:"))
        l.append(ele)

print(l)
s=0
for i in l:
    final=s+i
    s=final

print(final)

