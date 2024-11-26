def subarray(arr,size):
    maxx=arr[0]
    current=arr[0]

    for i in range(1,size):
        current=max(arr[i],current+arr[i])
        maxx=max(current,maxx)
        return maxx

arr=[]
size=int(input("ENTER SIZE"))
for i in range(0,size):
    n=int(input(f"Enter element "))
    arr.append(n)
maxx=subarray(arr,size)
print(maxx)
    
