#Write a python program to print odd numbers from n to 1
n = int(input("Enter a number: "))
for i in range(n if n % 2 != 0 else n - 1, 0, -2):
    print(i)    
    