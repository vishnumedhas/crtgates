#Write a python program to read an integer as input from user & check whether it is a three digit number or not?
num=int(input("Enter the integer:"))
#if-else
if(num>=100 and num<=999)or (num>=-999 and num<=-100):
    print(" Three Digit number")
else:
    print("number")
#ternary operator
res=" Three Digit number" if(num>=-99 and num<=99) or (num>=-99 and num<=-10) else "Number"
print(res)
