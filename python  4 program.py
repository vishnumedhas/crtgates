#Write a python program to read two integer values as input from user and find the largest number
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
#if-else
if(num1>num2):
    print(f"{num1} is largest number")
else:
    print(f"{num2} is largest number")
#ternary operator
res=num1 if(num1>num2) else num2
print(f"(res) is largest number,")

