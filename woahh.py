def diff(arr):
    arr.sort()
    suba=[]
    subb=[]
    for num in arr:
        if num>=0:
            suba.append(num)
        else:
            if not subb:
                subb.append(num)
            else:
                suba.append(num)
        
    suma=sum(suba)
    sumb=sum(subb)
    return abs(suma-sumb)

n=int(input())
arr=[]
arr = list(map(int, input("Enter the array elements: ").split()))
difference=diff(arr)
print(difference)
