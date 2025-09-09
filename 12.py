#Write a python program to read month number as a input from user and print the respective no of days in that particular month
m=int(input("Enter the month number:"))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print("31 days")
elif m==4 or m==6 or m==9 or m==11:
    print("30 days")
elif m==2:
    print("28 or 29 days")
else:
    print("Invalid month number")