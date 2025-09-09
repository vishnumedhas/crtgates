#You are building a water reminder. Input is the no of hours since user last drank water
#greater than 4 hours "You are dehydrated drink water now"
#between 2 to 4 hours "Drink a glass of water"
#less than 2 hours "You are fine"

hours = float(input("Enter hours since you last drank water: "))

if hours > 4:
    print("You are dehydrated drink water now")
elif hours >= 2:
    print("Drink a glass of water")
else:
    print("You are fine")