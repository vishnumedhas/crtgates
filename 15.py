#Write a python program to read an integer value as an input from user and check whether it is a multiple of 3 and 5 or not
num = int(input("Enter an integer: "))

if num % 3 == 0 and num % 5 == 0:
    print("It is a multiple of both 3 and 5")
else:
    print("It is not a multiple of both 3 and 5")