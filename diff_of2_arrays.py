def max_diff(a,arr):
    uni=set(arr)
    p=0
    n=0
    for num in uni:
        if num>0:
            p+=num
        elif num<0:
            n+=num

    diff=p-n
    return diff

a=int(input())
arr=list(map(int,input().split()))

result=max_diff(a,arr)
print(result)
