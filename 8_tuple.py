# Creating a tuple:
my_tuple = (1, 2, 3, "four", 5.6)
print(my_tuple)
# Output: (1, 2, 3, 'four', 5.6)


# Accessing elements of a tuple:
my_tuple = (1, 2, 3, "four", 5.6)

print(my_tuple[0])
# Output: 1

print(my_tuple[3])
# Output: 'four'


# Tuples can also be unpacked into individual variables:
my_tuple = (1, 2, 3)
a, b, c = my_tuple

print(a)
# Output: 1
print(b)
# Output: 2
print(c)
# Output: 3


# Tuples can be used as keys in a dictionary:
my_tuple = (1, 2, 3)
my_dict = {my_tuple: "value"}

print(my_dict[(1, 2, 3)])
# Output: 'value'


# Tuples can be converted to lists and vice versa:
my_tuple = (1, 2, 3)
my_list = list(my_tuple)

print(my_list)
# Output: [1, 2, 3]

my_tuple = tuple(my_list)

print(my_tuple)
# Output: (1, 2, 3)


# Tuples can be used to return multiple values from a function:
def get_name_and_age():
    name = "Alice"
    age = 25
    return name, age


result = get_name_and_age()

print(result)
# Output: ('Alice', 25)

name, age = get_name_and_age()

print(name)
# Output: 'Alice'

print(age)
# Output: 25
