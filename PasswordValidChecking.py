def validpass(passw):
    if len(passw)>20 or len(passw)<10:
        print("Very small pass")
        return
    if not any(char.isdigit() for char in passw):
        print("Must contain 1 digit")
        return
    if not any(char in "!@#$%^&*" for char in passw):
        print("must contain one symbol")
        return
    print("Valid password")


name = input("Enter your name: ")
mobile_number = input("Enter your mobile number: ")
username = input("Enter your username: ")
passw= input("Enter your password: ")

validpass(passw)
