# Enter the string content
main_str = input('please enter a string:')

letter_count = 0
num_count = 0
space_count = 0
other_count = 0

# Traversing characters in a string
for str in main_str:
    print(str)
    # Determine the type of each character
    if str.isalpha():
        # Calculated quantity
        letter_count += 1
    elif str.isspace():
        space_count += 1
    elif str.isdigit():
        num_count += 1
    else:
        other_count += 1
else:
    print('finished')

print(letter_count)

print(space_count)

print(num_count)

print(other_count)



