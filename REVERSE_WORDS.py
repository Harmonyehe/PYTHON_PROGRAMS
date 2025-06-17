def rev_fun(s):
    words=s.strip().split()
    rev=words[::-1]
    return ' '.join(rev)


s=input("ENter :")
print("Reverse is : ",rev_fun(s))