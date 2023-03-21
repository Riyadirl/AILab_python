# for loop

"""
for i in range(0, 5):
    print(i)
print("===loop ended===")


for i in range(0, 10, 2):
    print(i)


# nested loop

for i in range(6, 0, -2):
    for j in range(0, 2, 1):
        print(i, j)"""

# pattern
n = 5
for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()


# n = 5
# *********
# *******
# *****
# ***
# *

# x=4
# *
# **
# ***
# ****

n = 4
for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()

n = 5
for i in range(n, 0, -1):
    for j in range(2*i-1):
        print('*', end='')
    print()
