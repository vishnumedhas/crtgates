#restaurant gives discount based on the total bill:
#if the bill is more than $1000, apply a 10% discount
#if the bill is more than $500 , apply a 5% discount
#if bill less than or equal to $500, no discount
#write a program that takes the total bill amount and prints the final amount after applying the discount

bill = float(input("Enter the total bill amount: "))

if bill > 1000:
    discount = bill * 0.10
elif bill > 500:
    discount = bill * 0.05
else:
    discount = 0

final_amount = bill - discount
print(f"Final amount after discount: ${final_amount}")