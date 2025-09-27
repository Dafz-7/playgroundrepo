"""
-DONE add items to inventory
- remove items manually
- remove items when out of stock
- check current stock
- alert item if low on stock (less than 2)

- store items in a dictionary
- add menu loop

- save and load inventory from .txt or .json file (later)
"""

# functions
inventory_dict = {}
inventory_list = []

def add_items():
    while True:
        items = input("One item to add: ").lower()
        quantity = input("Amount in number(s): ")
        if quantity.isdigit():
            quantity = int(quantity)
            if 0 < quantity < 10000:
                break
            else:
                print("Amount must be > 0 and < 10000.")
        else:
            print("Please enter a valid number.")
    inventory_tuple = (items, quantity)
    inventory_list.append(inventory_tuple)
    for items, quantity in inventory_list:
        inventory_dict[items] = quantity

# Main program
print(
    """
    --- My inventory ---
    Type the following keywords:

    - add item
    - remove item
    - check inventory

    """
)

add_items()
print(inventory_list)
print(inventory_dict)

