#write a python program to read three integer values as a input from user and find the smallest number using both if else and ternary
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if((num1<num2) and (num1<num3)):
    print(f"{num1} is smallest number")
elif((num2<num3) and (num2<num1)):
    print(f"{num2} is smallest number")
else:
    print(f"{num3} is smallest number")
#ternary operator
smallest=num1 if(num1<num2 and num1<num3) else num2
res=num3 if(num3<num1 and num3<num2) else smallest
print(f"{res} is the smalest number")
