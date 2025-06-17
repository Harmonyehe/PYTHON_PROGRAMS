def freq_dig(s):
    freq=[0]*10

    while s>0:
        num=s%10
        freq[num]+=1
        s=s//10
    for i in range(10):
        if freq[i]>0:
            print(i,'->',freq[i])


n=int(input("Enter :"))
print(freq_dig(n))