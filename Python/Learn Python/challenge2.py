# simple guessing game

num = 1 # change num here
running = True
while running:
    try:
        user_num = int(input("Pick a number 1-10: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_num < num:
        print("Too low.")
    elif user_num > num:
        print("Too high.")
    else:
        print("You got it right!")
        running = False