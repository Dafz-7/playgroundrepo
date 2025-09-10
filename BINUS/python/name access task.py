# store a list of 5 names.
# ask the user to type their name.
# check if the name is in the list.

# no AI involved.

names = ["Agus", "Budi", "Rahmat", "Asep", "Hidayat"]
names_lower = [name.lower() for name in names]
repeat = True
while repeat:
    usertype = input("Type the name, is it on the list? Type: ").lower()
    if usertype in names_lower:
        print("Name is on the list.")
    else:
        print("Name is not on the list.")
        print("System exited.")
        repeat = False