#Write a python program and read an integer value as input and print FizzBuzz--> 3&5, Fizz-->3, Buzz-->5

num = int(input("Enter an integer: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)