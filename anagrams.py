def anagram(worda,wordb):
    worda=worda.replace(" ","").lower()
    wordb=wordb.replace(" ", "").lower()

    if len(worda)!=len(wordb):
        return False
    
    counta=[0]*26
    countb=[0]*26

    for char in worda:
        index=ord(char)-ord('a')
        counta[index]+=1

    for char in wordb:
        index=ord(char)-ord('a')
        countb[index]+=1

    return counta==countb

a=input("first word : ")
b=input("Second word : ")

if anagram(a,b):
    print("IS Anagram")
else:
    print("Not")

