# simple shopping list

shopping_list = []
running = True

print("here is your shopping list: ", shopping_list)
while running:
    items = input("Write the items to add (nothing if none): ").lower()
    if items == "nothing":
        pass
    else:
        shopping_list.append(items)

    check_list = input("Check your shopping list? ").lower()
    if check_list == "yes":
        print(shopping_list)
        remove_item = input("Want to remove certain item? ").lower()
        if remove_item == "yes":
            choose_item = input("Which one? ").lower()
            if choose_item in shopping_list:
                shopping_list.remove(choose_item)
            else:
                print("Item is not on the list.")
                continue
    else:
        pass

    add_more = input("Continue adding? ").lower()
    if add_more == "yes":
        running = True
    else:
        print("This is your final shopping_list: ", shopping_list)
        print("Thank you for shopping!")
        running = False