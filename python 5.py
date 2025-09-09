#Write a python program to read 2 integer value as input from user and find smallest number
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
#if-else
if(num1<num2):
    print(f"{num1} is smallest number")
else:
    print(f"{num2} is smallest number")
#ternary operator
res=num1 if(num1<num2) else num2
print(f"(res) is smallest number,")
