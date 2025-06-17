def pan(s):
    s=s.replace(" ", "").lower()
    if len(s)<26:
        return False
    
    check=[0]*26
    for char in s:
        index=ord(char)-ord('a')
        check[index]+=1

    for i in check:
        if i==0:
            return False
        
    return True





a=input("Enter : ")
if pan(a):
    print("Is a panagram")
else:
    print("Not a panagram")