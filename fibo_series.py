def fibo(n):
    a = 0
    b = 1
    print(a, b, end=' ')
    for _ in range(2, n):
        temp = a + b
        print(temp, end=' ')
        a = b
        b = temp

inp = int(input("Enter the length: "))
print("The series is:")
fibo(inp)  
