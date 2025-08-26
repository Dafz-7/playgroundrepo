random_number = [10, 13, 9, 8, 4, 11, 94, 110, 74]
largest_number_so_far = 0
for i in random_number:
    if i > largest_number_so_far:
        largest_number_so_far = i
print(f"Largest value: {largest_number_so_far}")