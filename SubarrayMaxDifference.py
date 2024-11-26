def diff(arr):
    arr.sort()   
    suba = []  
    subb = []  
 
    for num in arr:
        if num >= 0:
            suba.append(num) 
        else:
            if not subb: 
                subb.append(num)
            else:
                suba.append(num)  

    suma = sum(suba)
    sumb = sum(subb)
    return abs(suma - sumb)

n = int(input("Enter the size of the array: "))

arr = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

difference = diff(arr)

print("Maximum Difference =", difference)
