num=int(input("Enter the range: "))

odd=[]
for i in range(1,num):
    if i%2!=0:
        odd.append(i)

print("Odd numbers of the range give is:",odd)
