print('This is a Christmas Python list primer powered by the Cool Kitten Coding Café')
# We create a list. We start with giving it a name, then equal, then the two square brackets.
# Then inside we type each element between quotes
# Why do we use quotes? Because it's a list of strings, that is to say words.
my_christmas_list = ['candy cane', 'gingerbread man', 'christmas stocking']
# Let's print the list
print(my_christmas_list)
# Let's check its length and print the result
print('At the beginning the list has', len(my_christmas_list), 'items.')
# We append a new element, bells by using .append
my_christmas_list.append('bells')
# Let's print out the list and its length
print(my_christmas_list)
print('After appending bells, the list has', len(my_christmas_list), 'items.')
# We insert the element 'present' in the list at position 1 by using .insert
my_christmas_list.insert(1, 'present')
# Let's print out the list and its length
print(my_christmas_list)
print('After inserting present, the list has', len(my_christmas_list), 'items.')
# We add a list of elements at the end of your christmas list by using .extend
my_christmas_list.extend(['christmas tree', 'poinsettia'])
print(my_christmas_list)
print('After extending the list, the list has', len(my_christmas_list), 'items.')
# We find the position of an element within the index
print('Christmas tree is at position', my_christmas_list.index('christmas tree'), 'of the index.')
# We remove this element from the list
my_christmas_list.remove('christmas tree')
# We print out the list
print(my_christmas_list)
print('After removing christmas tree, the list has', len(my_christmas_list), 'items.')
# Bonus, not featured in the video, .pop.
# The pop command is a funny one,  it removes and return an element
my_christmas_list.pop(3)
print(my_christmas_list)
print('After popping the element at position 3, the list has', len(my_christmas_list), 'items.')
