#An employee works a standard 8 hours per day. If the employee works more than 8 hours, they get $100 per extra hour
#If not, display "No overtime pay". Write a program that takes the number of hours worked and prints overtime pay if applicable

hours = int(input("Enter number of hours worked: "))

if hours > 8:
    overtime_pay = (hours - 8) * 100
    print(f"Overtime pay: ${overtime_pay}")
else:
    print("No overtime pay")