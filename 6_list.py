# Creating an empty list:
my_list = []


# Creating a list with values:
my_list = [1, 2, 3, 4, 5]


# Accessing elements in a list:
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 4


# Changing elements in a list:
my_list = [1, 2, 3, 4, 5]
my_list[2] = 6
print(my_list)  # Output: [1, 2, 6, 4, 5]


# Slicing a list:
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3])  # Output: [2, 3]


# Adding elements to a list:
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]


# Removing an element from a list:
my_list = ["apple", "banana", "cherry"]
my_list.remove("banana")
print(my_list)  # Output: ['apple', 'cherry']


# Sorting a list:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]


#.
# Reversing a list:
my_list = ["apple", "banana", "cherry"]
my_list.reverse()
print(my_list)  # Output: ['cherry', 'banana', 'apple']
