full_name = 'Mr Potato Head' # Srings
has_pets = True # Booleans


# print(type(5)) # Integers
5.5 # Floats

# With Python the important part of the error message is on the bottom

# Python will not let us do type-coersion
# console.log(1 + '1') converts the number to a string => '1' + '1' => '11'
# print(1 + '1')

# Python has many of the same methods as JS
# but very different syntax
full_name = 'Mr Potato Head'

# In JS to get the length - full_name.length
# In Python - len(full_name)
len(full_name)


# Dictionaries (like objects in Js)

person = {
    'first_name': 'Emeril',
    'age': 54,
    'likes_cooking': True
}

# print(person['first_name'])

# In Python we can't access properties that don't exists
# In JS we can try to access properties that don't exists. returns => undefined
# print(person['has_pets'])

# Lists - Are like Arrays in JS
#               0              1           2
grocery_list = ['pizza dough', 'marinara', 'cheese']

# print(grocery_list[0])

# Goal is the get the last item in our list
# In JS - grocery_list[grocery_list.length - 1]
# In Python
# Gets the second to last item
# print(grocery_list[-2])

# Get the position of an item
print(grocery_list.index('marinara'))

#               0              1           2
grocery_list = ['pizza dough', 'marinara', 'cheese']

# Add items to a list
grocery_list.append('basil')
grocery_list.append('parmisan')

additions = ['mushrooms', 'tomato', 'pineapple']

# In Python we can combine lists with (+)
grocery_list = grocery_list + additions
grocery_list.extend(['serrano peppers', 'red peppers flakes'])


# Remove from a list
# In python we can remove a particular index
# grocery_list.pop(7)

# Can remove an item by it's name
grocery_list.remove('pineapple')

print(grocery_list)