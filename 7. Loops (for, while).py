# WHILE LOOPS
# While loops are used when you don't know ahead of time how many times you'll have to loop

import random
i = 5
while i < 15:
    print(i)
    i = i + 2

random_num = random.randrange(0, 10)

while (random_num != 5):
    print(random_num)
    random_num = random.randrange(0, 10)

# An iterator for a while loop is defined before the loop
i = 0
while (i <= 20):
    if(i % 2 == 0):
        print(i)
    elif(i == 9):
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue

    i += 1


# FOR LOOPS
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
for x in range(0, 10):
    print(x, ' ', end="")

print('\n')

# You can use for loops to cycle through a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

for y in grocery_list:
    print(y)

# You can also define a list of numbers to cycle through
for x in [2, 4, 6, 8, 10]:
    print(x)

# You can double up for loops to cycle through lists
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])


for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')
# hheellll  wwrrlldd

for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')
# hheellll

# for-else
for i in 'hello world':
    if i == 'a':
        break
else:
    print('There is no a')
# There is no a

# List comprehensions
# [2, 4, 6, ....]; [ ] is for list builder
evens1 = [x * 2 for x in range(1, 11)]
evens2 = [x for x in range(2, 21) if x % 2 == 0]  # evens1 == evens2
[y + 1 for y in evens1]  # [3, 5, 7...]
[z for z in evens1 if z >= 8]  # [8, 10, 12...]
