def count_vow(s):
    vowels="aeiouAEIOU"
    count=0
    for i in s:
        if i in vowels:
            count+=1

    return count

s=input("Enter the thing: ")
print("The number of vowels in the thing is : ",count_vow(s))