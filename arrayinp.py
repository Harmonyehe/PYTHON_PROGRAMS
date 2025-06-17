def sumofarray(arr):
    sums=0
    for i in arr:
        sums+=i
    return sums

arr=[]
a=int(input("Enter size of array: "))
for i in range(0,a):
    b=int(input())
    arr.append(b)

print("The array is",arr)
print("Sum of array elements is ",sumofarray(arr))