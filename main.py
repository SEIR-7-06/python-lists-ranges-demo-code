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
# print(grocery_list.index('marinara'))

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

# print(grocery_list)


# Tuples - Imutable set of data - cannot be changed
# Can be declared with or without ()
colors = ('red', 'green', 'blue')
colors = 'red', 'green', 'blue'

# colors.append('yellow')

# Get a section of a list or a tuple
#            0         1      2      3      4
students = ['Simone', 'Sri', 'Sam', 'Saly', 'Steve']

# In JavaScript - students.slice(0, 2)
# In Python
# Get a slice from the beginning up to index 2
# print(students[:2])

# Get a slice from second person to the end
# print(students[1:])

# Get a slice from second to last up to end
# print(students[-2:])

#            0         1      2      3      4
students = ['Simone', 'Sri', 'Sam', 'Saly', 'Steve']

# Create a clone of the students list
students_clone = students[:]
# print(students_clone)

user_info1 = 'a: sally smith'
user_info2 = 'r: Toni Giamatto'

# Just get me the 1st 2 characters of a string
# print(user_info1[:2])

# Just get the first character in a string
# print(user_info1[0])

########################################################
# Looping

# Ranges - Loop through a list of numbers
# for i in range(99, 0, -1):
#     print(f"{i} bottles of root beer on the wall...")


# for i in range(0, 100):
#     print(f"{i} bottles of root beer on the wall...")

##########################################################################
# For In Loop

grocery_list = ['pizza dough', 'marinara', 'cheese', 'basil']

# In JavaScript
# grocery_list.forEach((item, index) => {
#  console.log(index, item)
# })


# In Python
# for item in grocery_list:
#     print(item)


# 0. pizza dough (get this first!)
# 1. marinara
# 2. cheese
for index, item in enumerate(grocery_list):
    if index == 0:
        print(f"{index + 1}. {item} (get this first!)")

    else:
        print(f"{index + 1}. {item}")


grocery_list = ['pizza dough', 'marinara', 'cheese', 'basil']

# Check if basil in the list
for item in grocery_list:
    if item == 'basil':
        print('You remembered!!!')


#############################################################
# Print 'You forgot if basil is not in the list
you_forgot = True

for item in grocery_list:
    if item == 'basil':
        you_forgot = False
        print('You remembered!!!')

if you_forgot:
    print('You forgot!')

##############################################################
# In JavaScript
# === - Strict equality 1 === '1' => false
# == - loose equality 1 == '1' => true

# In Python
# We only have stict equality
# with ==

