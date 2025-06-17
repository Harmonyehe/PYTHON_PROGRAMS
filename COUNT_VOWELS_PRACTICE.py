def count_vowels(s):
    vowels='aeiouAEIOU'
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count



s=input("Enter the thing : ")
print("the numebr of vowels is: ",count_vowels(s))