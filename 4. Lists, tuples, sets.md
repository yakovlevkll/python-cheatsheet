# Advanced structures

## Lists

A list is like an apartment house. Each room has it's own number (index) and contains some data - maybe amount of people in it, maybe something else.

Another way is to think about it like a box with boxes. Outside box is a list itself, inner boxes are values (almost like variables), each of them stores some information. We can access this information using name of the list and index of a inner box.

When can it be helpful? One of the common situations is when we need to store some similar pieces of data - maybe list with names, or phone numbers, or maybe coordinates or else.

```python
grocery = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
item = grocery[0]  # >>> 'Juice'
```

In other programming languages lists are often named as _array_.

We can change the value stored in a list (thing that we can't do with strings)

```python
grocery[0] = "Green Juice"
# >>> ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas']
```

As with strings, we can get a subset of the list with `[start_index:end_index]` but not including value on `end_index`.

```python
grocery[1:3]  # >>> ['Tomatoes', 'Potatoes']
```

We can put any data type in a a list including another lists. As a result we will have multi-dimensional lists

```python
events = ['Wash Car', 'Pick up Kids', 'Cash Check']
to_do = [events, grocery]
# >>>

to_do[1][0]
# >>> (first item in the second sublist)
```

>> The good practice is not to store different types of data in one list. Use `dict` instead (you can read about it in corresponding chapter).

### Basic operations

```python
new_list = events + grocery  # merge  lists
# >>>

grocery.append('onions')
# >>>

grocery.insert(1, "Pickle")
# >>>

grocery.sort()
# >>>

grocery.reverse()
# >>>

grocery.remove("Pickle")
# >>>

del grocery[4]
# >>>
```

Another very useful block of operations

```python
values = [1, 3, -2, 0]

len(values)  # >>> 4 (amount of values in list)
min(values)  # >>> -2 (minimum value in list)
max(values)  # >>> 3 (maximum value in list)
sum(values)  # >>> 2 (sum of all value in list)
```

### Range

There is handsome `range` operation to generate lists with numbers in Python

```python
a = range(4)  # >>> range(4)
list(range(5, 9))  # >>> [5, 6, 7, 8]
```

It can even more, read the docs.

## Tuples

Values in a tuple can't be changed like values in a list

```python
pi_tuple = (3, 1, 4, 1, 5, 9)
```

Operations as `len`, `max`, `min` and `sum` also available with tuples.

## Sets

```python
arr = [1, 2, 3, 2, 4, 1, 1]
set(arr)  # >>> (1, 2, 3, 4)
```

## Converting

We can use `list`, `tuple` and `set` commands to convert from one array type to another

```python
new_tuple = list(pi_tuple)
new_list = tuple(grocery)
new_set = set(pi_tuple)
```

If we try to convert string into list

```python
list("Hello")  # >>> ['H', 'e', 'l', ....]
```

## Matrices

_Note. It is recommended to study Cycles chapter first._

One specific application of lists and tuples is mathematical matrices. We can obtain multi-dimensional structures.

```python
cols = 8
rows = 5

M = [[0 for x in range(cols)] for x in range(rows)]  # create zero matrix

# M[6][0] = 3  # >>> ERROR - out of range
M[0][6] = 3
print(M[0][6])  # >>> 3
```

Or with short syntax

```python
M = [[0] * cols for i in range(rows)]
```

You can use `numpy`, `pandas` or any similar package to work with matrices and other math stuff in Python.

```python
import numpy

numpy.zeros((5, 5))
'''array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])'''
numpy.matrix([[1, 2], [3, 4]])
'''matrix([[1, 2],
        [3, 4]])'''

numpy.matrix('1 2; 3 4')
numpy.arange(25).reshape((5, 5))
numpy.array(range(25)).reshape((5, 5))
numpy.ndarray((5, 5))
```