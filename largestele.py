def largest(arr):
    large=arr[0]

    for i in arr:
        if i>large:
            large=i

    return large

arr=[]
n=int(input("Enter size :"))
for i in range(0,n):
    b=int(input())
    arr.append(b)

print("The array is ",arr)
print("The largest elemet is ",largest(arr))