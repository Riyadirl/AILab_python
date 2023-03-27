# Filtering a list of numbers to get only even numbers:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4, 6, 8, 10]


# Filtering a list of strings to get only strings that contain a certain substring:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits_with_a = list(filter(lambda x: 'a' in x, fruits))
print(fruits_with_a)
# Output: ['apple', 'banana', 'mango']


# Filtering a dictionary to get only key-value pairs that satisfy a certain condition:

ages = {"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}

over_30 = dict(filter(lambda x: x[1] > 30, ages.items()))
print(over_30)
# Output: {'Charlie': 35, 'David': 40}


# Filtering a list of tuples to get only tuples where the second element is greater than the first:

tuples = [(1, 5), (3, 2), (7, 9), (4, 4)]

greater_second = list(filter(lambda x: x[1] > x[0], tuples))
print(greater_second)
# Output: [(1, 5), (3, 2), (7, 9)]


# Filtering a list of objects to get only objects of a certain type:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 35)]

over_30 = list(filter(lambda x: x.age > 30, people))
print(over_30)
# Output: [Person(name='Bob', age=30), Person(name='Charlie', age=35)]
