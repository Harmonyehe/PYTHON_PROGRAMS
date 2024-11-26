
def subarraysum(arr,n):
    max_sum=arr[0]
    curr_max=arr[0]
    for i in range(1,len(arr)):
                   curr_max=max(arr[i],curr_max+arr[i])
                   max_sum=max(max_sum,curr_max)
    return max_sum
arr=[]
size=int(input("Enter"))
for i in range(0,size):
    num=int(input())

    arr.append(num)

max_sum=subarraysum(arr,size)
print(max_sum)
