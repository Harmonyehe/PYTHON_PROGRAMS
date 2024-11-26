def inttoroman(number):
    val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    sym=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    rom_num=""
    for i in range(len(val)):
        while number >= val[i]:
            rom_num+=sym[i]
            number-=val[i]
    return rom_num

number=int(input("Enter"))
print("Roman Number:",inttoroman(number))
    
