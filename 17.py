#Write a python program to read amount as input from user and print no of notes required in indian currency dimensions
amount = int(input("Enter the amount: "))

notes = [ 500, 200, 100, 50, 20, 10, 5, 2, 1]
note_count = {}

remaining = amount

for note in notes:
    count = remaining // note
    if count > 0:
        note_count[note] = count
        remaining = remaining % note

print("Notes required:")
for note in notes:
    if note in note_count:
        print(f"{note} : {note_count[note]}")