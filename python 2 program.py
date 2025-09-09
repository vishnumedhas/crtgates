# write a python program to read an integer value and check whether it is a digit or a number
num=int(input("Enter the integer:"))
#if-else
if(num>=-9 and num<=9):
    print("Digit")
else:
    print("number")
#ternary operator
res="Digit" if(num>=-9 and num<=9) else "Number"
print(res)
