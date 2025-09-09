#Write a python program in a theater, ticket prices vary depending on customers age:
#child below 12 years -$150
#Teenagers between 12 and 18 years -$200
#Adults above 18 years -$300
#Write a program that asks the user for their age and then displays the ticket price.

age = int(input("Enter your age: "))

if age < 12:
    price = 150
elif age <= 18:
    price = 200
else:
    price = 300

print(f"Ticket price: ${price}")
