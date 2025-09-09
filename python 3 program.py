#Write a python program to read integer as Input from user and check whether it is a two digit num or not a two digit num
num=int(input("Enter the integer:"))
#if-else
if(num>=10 and num<=99)or (num>=-99 and num<=-10):
    print(" Two Digit number")
else:
    print("number")
#ternary operator
res=" two Digit number" if(num>=-99 and num<=99) or (num>=-99 and num<=-10) else "Number"
print(res)
