#Write a python program to read the month number as input from the user and check whether it is valid month or not
month=int(input("Enter the month number(1-12:)"))
if 1<= month <=12:
    print(f"{month} is a valid month number")
else:
    print(f"{month} is not a valid month number")
